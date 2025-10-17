import json
from typing import List, Dict
from .translate import translate_lines
from .prompts import SYSTEM, USER_TEMPLATE

# TODO: wire your LLM provider here
def call_llm(system, user):
    raise NotImplementedError("Wire your LLM API here and return the assistant text.")

def generate_items(ar_facts: List[str], n_mcq=6, n_tf=4, n_cloze=4):
    en_facts = translate_lines(ar_facts)
    facts_str = "\n".join(f"{i} | {s}" for i,s in enumerate(en_facts))
    prompt = USER_TEMPLATE.format(facts=facts_str, n_mcq=n_mcq, n_tf=n_tf, n_cloze=n_cloze)
    raw = call_llm(SYSTEM, prompt)
    data = json.loads(raw)
    # simple validator
    clean=[]
    for it in data:
        if it.get("type") == "MCQ":
            ch = it.get("choices", [])
            if not (isinstance(ch, list) and len(ch) == 4 and it.get("answer") in ch):
                continue
        ids = it.get("fact_ids", [])
        if not ids or max(ids) >= len(en_facts):
            continue
        clean.append(it)
    return clean, en_facts
