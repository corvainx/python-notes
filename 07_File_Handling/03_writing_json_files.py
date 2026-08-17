# Lesson 03: Serializing Data to JSON (json.dump)
import json
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(base_dir, "data", "output.json")

user_data = {
    "username": "dexter_morgan",
    "name": "Dexter Morgan",
    "role": "Forensic Analyst",
    "age": 35,
    "skills": ["Python", "Algorithms", "Forensics"],
    "is_active": True
}

with open(json_path, "w", encoding="utf-8") as f:
    json.dump(user_data, f, indent=4)

print(f"JSON data successfully serialized to: {json_path}")
