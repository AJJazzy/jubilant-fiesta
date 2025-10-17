import numpy as np, faiss
from sentence_transformers import SentenceTransformer
from .settings import EMB_MODEL, FAISS_PATH

_model = SentenceTransformer(EMB_MODEL)
_index = None

def embed(texts):
    return _model.encode(texts, batch_size=64, normalize_embeddings=True)

def get_index():
    global _index
    if _index is None:
        try:
            _index = faiss.read_index(str(FAISS_PATH))
        except Exception:
            _index = faiss.IndexFlatIP(384)
    return _index

def add_to_index(vecs):
    idx=get_index(); idx.add(vecs.astype('float32'))
    faiss.write_index(idx, str(FAISS_PATH))

def search(q_vec, k=8):
    idx=get_index(); D,I=idx.search(q_vec.astype('float32'), k)
    return D,I
