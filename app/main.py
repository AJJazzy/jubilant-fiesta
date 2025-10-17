from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import HTMLResponse, FileResponse
from pathlib import Path
from .db import init_db
from .ingest import pdf_to_arabic_text, to_facts
from .quizgen import generate_items
from .export_docx import export

app=FastAPI(); init_db()

INDEX = Path("static/index.html").read_text(encoding="utf-8")

@app.get("/", response_class=HTMLResponse)
def home():
    return INDEX

@app.post("/generate")
async def generate(file: UploadFile, n_mcq: int = Form(6), n_tf: int = Form(4), n_cloze: int = Form(4)):
    tmp = Path("/tmp/upload.pdf"); tmp.write_bytes(await file.read())
    ar = pdf_to_arabic_text(str(tmp))
    facts = to_facts(ar)
    items, en_facts = generate_items(facts, n_mcq, n_tf, n_cloze)
    out = Path("/tmp/quiz.docx")
    export(items, facts, en_facts, path=str(out))
    return FileResponse(str(out), filename="quiz.docx")
