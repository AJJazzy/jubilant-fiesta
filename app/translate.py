from transformers import MarianMTModel, MarianTokenizer
import hashlib, json
from pathlib import Path
from .settings import MT_MODEL, GLOSSARY, CACHE_DIR

_tok = MarianTokenizer.from_pretrained(MT_MODEL)
_mod = MarianMTModel.from_pretrained(MT_MODEL)

_cache_file = CACHE_DIR/"mt_cache.json"
try:
    _cache = json.loads(_cache_file.read_text(encoding="utf-8"))
except Exception:
    _cache = {}

def translate_lines(lines):
    out=[]; batch=[]; idx=[]
    for ln in lines:
        key=hashlib.md5(ln.encode('utf-8')).hexdigest()
        if key in _cache:
            out.append(_cache[key]); continue
        prot=ln
        for ar,en in GLOSSARY.items():
            prot = prot.replace(ar,f"[[[{en}]]]")
        batch.append(prot); idx.append(key)
        if len(batch)==32:
            _flush(batch, idx, out); batch=[]; idx=[]
    if batch: _flush(batch, idx, out)
    _cache_file.write_text(json.dumps(_cache, ensure_ascii=False), encoding="utf-8")
    return out

def _flush(batch, idx, out):
    enc=_tok(batch, return_tensors="pt", padding=True, truncation=True, max_length=512)
    gen=_mod.generate(**enc, max_length=512)
    dec=_tok.batch_decode(gen, skip_special_tokens=True)
    for k,t in zip(idx,dec):
        t = t.replace("[[[", "").replace("]]]", "")
        _cache[k]=t; out.append(t)