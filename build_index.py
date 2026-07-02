import json
from pathlib import Path

root = Path(".")
files = []

for p in root.rglob("*.md"):
    files.append(str(p).replace("\\", "/"))

files.sort()

with open("files.json", "w", encoding="utf-8") as f:
    json.dump(files, f, indent=2)

print("files.json generated")