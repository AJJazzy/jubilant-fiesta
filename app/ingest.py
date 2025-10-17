import hashlib, io, re
from typing import List
import fitz
from PIL import Image
import pytesseract

AR_SENT_SPLIT = re.compile(r"(?<=[\.!\?؟])\s+|\n+")

def pdf_to_arabic_text(path: str) -> str:
    doc = fitz.open(path)
    chunks=[]
    for p in doc:
        t=p.get_text().strip()
        if not t:
            # scanned page
            pix=p.get_pixmap(dpi=300)
            img=Image.open(io.BytesIO(pix.tobytes("png")))
            t=pytesseract.image_to_string(img, lang="ara")
        if t: chunks.append(t)
    return "\n".join(chunks)

def to_facts(ar_text: str) -> List[str]:
    sents=[x.strip() for x in AR_SENT_SPLIT.split(ar_text) if len(x.split())>=4]
    return dedup(sents)

def dedup(sents: List[str]) -> List[str]:
    seen=set(); out=[]
    for s in sents:
        h=hashlib.sha1(s.encode('utf-8')).hexdigest()
        if h not in seen:
            seen.add(h); out.append(s)
    return out
