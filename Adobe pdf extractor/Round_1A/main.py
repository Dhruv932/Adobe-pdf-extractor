import os
import json
import time

from layout_parser import detect_headings, load_fallback, is_heading_noise, is_probably_body

INPUT_DIR   = "input"
OUTPUT_DIR  = "output"
TRUTH_DIR   = "truth"  

os.makedirs(OUTPUT_DIR, exist_ok=True)

import re

def normalize(text):
    
    text = text.lower().strip()
    text = text.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    text = re.sub(r'[^\w\s]', '', text)  
    return text


gbt = load_fallback()

for fname in sorted(os.listdir(INPUT_DIR)):
    if not fname.lower().endswith(".pdf"):
        continue

    path = os.path.join(INPUT_DIR, fname)
    start = time.time()

    
    heads = detect_headings(path, fallback=gbt)


    title_parts = []
    for h in heads:
        if h["level"] == "H1" and h["page"] == 1 \
        and not is_heading_noise(h["text"]) \
        and not is_probably_body(h["text"], h.get("size", 0), 0, h.get("gap", 0)):
            title_parts.append(h["text"].strip())

    title = " ".join(title_parts) if title_parts else ""

    outline = [
        { "level": h["level"], "text": h["text"].strip(), "page": h["page"] - 1 }
        for h in heads
        if not (h["level"] == "H1" and h["page"] == 1)
        and not is_heading_noise(h["text"])
        and not is_probably_body(h["text"], h.get("size", 0), 0, h.get("gap", 0))
        and len(h["text"].strip()) > 3 
    ]

    if not title:
        outline = [
            { "level": h["level"], "text": h["text"].strip(), "page": h["page"] - 1 }
            for h in heads
            if h["level"] == "H1"
            and not is_heading_noise(h["text"])
            and not is_probably_body(h["text"], h.get("size", 0), 0, h.get("gap", 0))
            and len(h["text"].strip()) > 3
        ]

    data = {"title": title, "outline": outline}

    out_path = os.path.join(OUTPUT_DIR, fname[:-4] + ".json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    elapsed = time.time() - start
    msg = f"{fname} → {elapsed:.2f}s"

    truth_path = os.path.join(TRUTH_DIR, fname[:-4] + ".json")
    if os.path.exists(truth_path):
        truth = json.load(open(truth_path, encoding="utf-8"))["outline"]
        
    print(msg)