# Python Fundamentals — Lesson 7: File Handling & Serialization

> **Goal:** Master filesystem interactions in Python: file detection, context managers (`with`), read/write access modes, plain text processing, structured JSON serialization, and CSV tabular record parsing.

---

# Table of Contents
1. [The Context Manager (`with open`)](#1-the-context-manager-with-open)
2. [File Open Modes Matrix](#2-file-open-modes-matrix)
3. [Path Resolution and OS Portability](#3-path-resolution-and-os-portability)
4. [Text File Operations](#4-text-file-operations)
5. [JSON Serialization (`json` module)](#5-json-serialization-json-module)
6. [CSV Processing (`csv` module)](#6-csv-processing-csv-module)
7. [Key Takeaways](#7-key-takeaways)

---

# 1. The Context Manager (`with open`)

Always access files through context managers (`with` statement). This guarantees that OS file descriptors are automatically closed upon exit, even if unhandled exceptions occur.

```python
with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()
# File is guaranteed to be closed here!
```

---

# 2. File Open Modes Matrix

| Mode | Purpose | File Must Exist? | Position | Truncates? |
| :--- | :--- | :--- | :--- | :--- |
| `'r'` | Read only (default) | **Yes** | Start | No |
| `'w'` | Write only | No (creates) | Start | **Yes (wipes old data)** |
| `'a'` | Append only | No (creates) | End | No |
| `'x'` | Exclusive creation | **Must NOT exist** | Start | No |
| `'r+'`| Read and Write | **Yes** | Start | No |
| `'b'` | Binary mode flag (e.g. `'rb'`) | - | - | - |

---

# 3. Path Resolution and OS Portability

Never hardcode platform-specific paths like `C:\path` or `/home/user/...`. Construct paths relative to the current file using `os.path` or modern `pathlib`:

```python
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_dir, "data", "sample.txt")
```

---

# 4. Text File Operations

- `file.read()`: Reads entire file into a single `str` (caution on huge files).
- `file.readline()`: Reads a single line.
- `for line in file:`: **Best Practice.** Streams lines lazily with $O(1)$ memory usage.
- `file.write(s)`: Writes string to file.
- `file.writelines(list_of_strings)`: Writes list of strings.

---

# 5. JSON Serialization (`json` module)

| Operation | From Memory | To/From File |
| :--- | :--- | :--- |
| **Serialize (Encode)** | `json.dumps(obj, indent=4)` | `json.dump(obj, file, indent=4)` |
| **Deserialize (Decode)** | `json.loads(json_string)` | `json.load(file)` |

---

# 6. CSV Processing (`csv` module)

- `csv.reader(file)` / `csv.writer(file)`: Row-by-row lists.
- `csv.DictReader(file)` / `csv.DictWriter(file)`: Maps rows to fieldname-keyed dictionaries.

---

# 7. Key Takeaways

1. **Always specify `encoding="utf-8"`** to ensure cross-platform character safety.
2. **Stream large files using `for line in file:`** rather than loading everything into memory.
3. **Use `json` for structured data and `csv` for spreadsheet/tabular datasets.**
