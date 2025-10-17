from pathlib import Path
DATA_DIR = Path("./data"); DATA_DIR.mkdir(exist_ok=True)
CACHE_DIR = DATA_DIR/"cache"; CACHE_DIR.mkdir(exist_ok=True)
DB_PATH = DATA_DIR/"app.sqlite3"
FAISS_PATH = DATA_DIR/"faiss.index"
MT_MODEL = "Helsinki-NLP/opus-mt-ar-en"
EMB_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
BATCH = 32
GLOSSARY = {
    "الاقتصاد الكلي": "macroeconomics",
    "الاقتصاد الجزئي": "microeconomics",
    "المواطنة": "civics",
    "العولمة": "globalization",
}
