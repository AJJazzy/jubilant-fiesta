import sqlite3
from .settings import DB_PATH

def get_conn():
    con = sqlite3.connect(DB_PATH); con.row_factory = sqlite3.Row; return con

def init_db():
    con=get_conn(); cur=con.cursor()
    cur.executescript('''
    CREATE TABLE IF NOT EXISTS documents(
      id INTEGER PRIMARY KEY, title TEXT, created_at TEXT
    );
    CREATE TABLE IF NOT EXISTS facts(
      id INTEGER PRIMARY KEY, doc_id INT, topic TEXT, ar TEXT, en TEXT, span_hash TEXT UNIQUE
    );
    CREATE TABLE IF NOT EXISTS embeddings(
      fact_id INT PRIMARY KEY, vec BLOB
    );
    CREATE TABLE IF NOT EXISTS items(
      id INTEGER PRIMARY KEY, fact_ids TEXT, type TEXT, stem TEXT, choices_json TEXT, answer TEXT, rubric TEXT, created_at TEXT
    );
    '''); con.commit(); con.close()
