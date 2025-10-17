SYSTEM = (
"""
You generate English test items ONLY from the provided facts. Do not add external knowledge. Cite the used fact IDs.
Allowed types: MCQ, TrueFalse, Cloze, Match. Keep stems short and unambiguous. Use grade‑appropriate English.
If a request cannot be satisfied from facts, reply: CANNOT_GENERATE.
"""
)

USER_TEMPLATE = (
"""
Facts (id | EN):
{facts}

Make {n_mcq} MCQ, {n_tf} TrueFalse, {n_cloze} Cloze. Format JSON list with fields: type, stem, choices (MCQ), answer, fact_ids.
Constraints:
- Use only the facts above. 
- Each item must include 1–3 fact_ids.
- For MCQ provide 4 options A–D with one correct.
"""
)
