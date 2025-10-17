# Teacher‑Fed English Test Generator (Full Stack MVP)

## What it does
- Ingest Arabic notes/books (PDF, scanned images).
- Translate to English with a controlled glossary.
- Build a fact KB and generate **English** quizzes strictly from fed content.
- Cite Arabic evidence under each item. Export DOCX.

## Requirements
- OS: Windows 10/11, macOS, or Linux.
- Python: 3.10–3.12 recommended.
- Packages: see `requirements.txt`.
- Tesseract OCR with Arabic language data:
  - **Windows**: Install the UB Mannheim Tesseract build. During setup, select *Arabic*.
  - **macOS**: `brew install tesseract && brew install tesseract-lang` (or place `ara.traineddata` under `/usr/local/share/tessdata` or `/opt/homebrew/share/tessdata`).
  - **Linux (Debian/Ubuntu)**: `sudo apt-get install tesseract-ocr tesseract-ocr-ara`.

## Quick start
```bash
python -m venv venv
# Windows
venv\Scripts\pip install -r requirements.txt
# macOS/Linux
source venv/bin/activate && pip install -r requirements.txt

# Run server
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000/ and upload a PDF.

## Configure
- Glossary: edit `app/settings.py` → `GLOSSARY`.
- LLM: implement API call in `app/quizgen.py` → `call_llm` (temperature=0).

## Notes
- OCR and MT are batched and cached for speed.
- Every generated item must cite fact IDs; evidence can be toggled in exporters.
