# Lesson 06: Deserializing JSON Data (json.load)
import json
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(base_dir, "data", "output.json")

try:
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    print("Parsed JSON Record:")
    print(f"Name: {data.get('name')}")
    print(f"Role: {data.get('role')}")
    print(f"Skills: {', '.join(data.get('skills', []))}")
except FileNotFoundError:
    print(f"File not found. Run 03_writing_json_files.py first to generate {json_path}")
