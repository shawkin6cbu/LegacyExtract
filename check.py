# convert_to_jsonl.py
#
# Reads every .txt file in C:\Scripts\extracted_text
# and writes train.jsonl in the same folder.
#
# Each JSONL line looks like:
# {"text": "full contract text …", "entities": []}

import json
import pathlib

# ---------- paths ----------
INPUT_DIR = pathlib.Path(r"C:\Scripts\extracted_text")
OUTPUT_FILE = INPUT_DIR / "train.jsonl"

# ---------- conversion ----------
with OUTPUT_FILE.open("w", encoding="utf-8") as outfile:
    for txt_path in sorted(INPUT_DIR.glob("*.txt")):
        text = txt_path.read_text(encoding="utf-8").strip()
        record = {"text": text, "entities": []}  # add spans later
        json_line = json.dumps(record, ensure_ascii=False)
        outfile.write(json_line + "\n")

print(f"✅ Wrote {OUTPUT_FILE} with {len(list(INPUT_DIR.glob('*.txt')))} documents.")
