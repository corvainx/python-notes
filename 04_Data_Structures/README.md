# Python Fundamentals — Lesson 4: Data Structures & Collections

> **Goal:** Deeply analyze Python's 4 core built-in data structures: Lists, Sets, Tuples, and Dictionaries. Understand mutability, internal memory layout, time complexity, and selection criteria.

---

# Table of Contents
1. [Data Structure Comparison Matrix](#1-data-structure-comparison-matrix)
2. [Lists (`list`)](#2-lists-list)
3. [Sets (`set`)](#3-sets-set)
4. [Tuples (`tuple`)](#4-tuples-tuple)
5. [Dictionaries (`dict`)](#5-dictionaries-dict)
6. [Multidimensional Structures](#6-multidimensional-structures)
7. [Time Complexity Cheat Sheet](#7-time-complexity-cheat-sheet)
8. [Key Takeaways](#8-key-takeaways)

---

# 1. Data Structure Comparison Matrix

| Data Structure | Syntax | Ordered? | Mutable? | Duplicates? | Indexable? | Use Case |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **List** | `[...]` | Yes | **Yes** | Yes | Yes | Dynamic sequential data |
| **Tuple** | `(...)` | Yes | **No** | Yes | Yes | Fixed records, read-only data |
| **Set** | `{...}` | No | **Yes** | **No** | No | Unique elements, membership, set algebra |
| **Dictionary** | `{k: v}` | Yes (3.7+) | **Yes** | Keys: No / Vals: Yes | By Key | Fast key-value lookups |

---

# 2. Lists (`list`)

Lists are dynamically resized arrays storing references to objects:

```text
List [0x100] ──> [ Ref0 | Ref1 | Ref2 | Ref3 ]
                   │      │      │      │
                   ▼      ▼      ▼      ▼
                "apple" "banana" 42   True
```

- Append: `list.append(x)` — $O(1)$ amortized.
- Insert: `list.insert(i, x)` — $O(N)$ due to shifting elements.
- Delete: `list.remove(val)` or `list.pop(i)` — $O(N)$.

---

# 3. Sets (`set`)

Sets are implemented via hash tables without associated values:

```text
Hash Table Buckets:
  hash("apple")  ──> Bucket 3 ──> "apple"
  hash("banana") ──> Bucket 7 ──> "banana"
```

- Lookup/Insert/Delete: Average $O(1)$.
- All set elements must be **hashable** (immutable: ints, floats, strings, tuples).

---

# 4. Tuples (`tuple`)

Tuples are lightweight, immutable sequences:
- Memory overhead is lower than lists because size and content are fixed.
- Excellent for dictionary keys and unpacking return values:

```python
point = (10, 20)
x, y = point  # Tuple unpacking
```

---

# 5. Dictionaries (`dict`)

Python dictionaries are compact hash maps mapping keys to values:
- Average $O(1)$ key lookup, insertion, and deletion.
- `.get(key, default)` avoids `KeyError` on missing keys.
- Dict views (`.keys()`, `.values()`, `.items()`) provide dynamic iterable views.

---

# 6. Multidimensional Structures

Matrices and grids can be represented as lists-of-lists or tuples-of-tuples:

```text
Matrix[row][col]:
             Col 0   Col 1   Col 2
    Row 0 [   1   ,   2   ,   3   ]
    Row 1 [   4   ,   5   ,   6   ]
    Row 2 [   7   ,   8   ,   9   ]
```

---

# 7. Time Complexity Cheat Sheet

| Operation | List | Set | Dict |
| :--- | :--- | :--- | :--- |
| Index Access `obj[i]` | $O(1)$ | N/A | $O(1)$ (key) |
| Search `x in obj` | $O(N)$ | $O(1)$ | $O(1)$ (key) |
| Append / Insert End | $O(1)$ | $O(1)$ (add) | $O(1)$ |
| Arbitrary Insert | $O(N)$ | N/A | $O(1)$ |
| Delete | $O(N)$ | $O(1)$ | $O(1)$ |

---

# 8. Key Takeaways

1. **Choose Set for uniqueness and fast membership queries.**
2. **Choose Tuple for immutable fixed records.**
3. **Choose Dictionary for structured entity mappings.**
4. **Choose List for ordered sequences requiring frequent sorting or modification.**
