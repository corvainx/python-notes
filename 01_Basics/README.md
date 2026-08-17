# Python Fundamentals — Lesson 1: Basics

> **Goal:** Master core Python building blocks: variable representation, dynamic typing, typecasting rules, user I/O, mathematical operations, and string manipulation.

---

# Table of Contents
1. [How Python Works Internally](#1-how-python-works-internally)
2. [Variables and Dynamic Typing](#2-variables-and-dynamic-typing)
3. [Typecasting Mechanics](#3-typecasting-mechanics)
4. [User Input and Terminal I/O](#4-user-input-and-terminal-io)
5. [Arithmetic and Augmented Assignment](#5-arithmetic-and-augmented-assignment)
6. [Built-in Math & the Math Module](#6-built-in-math--the-math-module)
7. [String Methods](#7-string-methods)
8. [String Indexing and Slicing](#8-string-indexing-and-slicing)
9. [Format Specifiers (f-strings)](#9-format-specifiers-f-strings)
10. [Key Takeaways](#10-key-takeaways)

---

# 1. How Python Works Internally

Python is an interpreted, high-level language. When you run a script:

```text
Source Code (.py)
      │
      ▼
   Compiler
 (CPython Parser)
      │
      ▼
 Bytecode (.pyc)
      │
      ▼
Python Virtual Machine (PVM)
      │
      ▼
  CPU Execution
```

- Unlike compiled languages (C/C++) that produce machine binaries directly, Python generates platform-independent bytecode evaluated by the Python Virtual Machine (PVM).
- Everything in Python is an **object**, and variables are **references (pointers)** to those objects in heap memory.

---

# 2. Variables and Dynamic Typing

In Python, you do not declare types explicitly. The interpreter binds names to object references dynamically.

```text
variable_name ──(reference)──> [ Object in Memory | Type: int | Value: 25 ]
```

### Core Primitive Data Types:
| Type | Description | Example |
| :--- | :--- | :--- |
| `str` | Textual string sequences | `"Dexter"`, `'Python'` |
| `int` | Arbitrary precision integers | `42`, `-100`, `1_000_000` |
| `float` | Double precision floating-point | `3.14159`, `-0.001` |
| `bool` | Boolean truth values | `True`, `False` |

---

# 3. Typecasting Mechanics

Typecasting converts a value from one data type to another:
- `int(x)`: Converts to integer (truncates floats toward zero).
- `float(x)`: Converts to floating point.
- `str(x)`: Converts object into its string representation.
- `bool(x)`: Evaluates "truthiness".

### Truthiness Matrix
In Python, values are considered `False` if they are:
- `0`, `0.0`, `0j`
- Empty sequences or collections: `""`, `[]`, `()`, `{}`, `set()`
- `None` and `False`

All other values evaluate to `True`.

---

# 4. User Input and Terminal I/O

The built-in `input(prompt)` function pauses execution, prints the prompt to standard output, and captures user input as a `str`.

```python
name = input("Enter name: ")       # Returns str
age = int(input("Enter age: "))    # Cast immediately to int for numerical operations
```

---

# 5. Arithmetic and Augmented Assignment

| Operator | Operation | Example | Result |
| :--- | :--- | :--- | :--- |
| `+` | Addition | `5 + 2` | `7` |
| `-` | Subtraction | `5 - 2` | `3` |
| `*` | Multiplication | `5 * 2` | `10` |
| `/` | True Division | `5 / 2` | `2.5` (always float) |
| `//` | Floor Division | `5 // 2` | `2` (rounds down) |
| `%` | Modulo (Remainder) | `5 % 2` | `1` |
| `**` | Exponentiation | `5 ** 2` | `25` |

---

# 6. Built-in Math & the Math Module

### Built-in Math Functions:
- `round(number, digits)`: Rounds to $n$ decimal places (uses Banker's rounding).
- `abs(number)`: Computes magnitude $|x|$.
- `pow(base, exp)`: Computes $base^{exp}$.
- `max(a, b, ...)` & `min(a, b, ...)`: Returns extremum.

### `import math` Module:
- `math.pi`, `math.e`: Mathematical constants.
- `math.sqrt(x)`: Square root $\sqrt{x}$.
- `math.ceil(x)`: Ceiling function $\lceil x \rceil$ (rounds up).
- `math.floor(x)`: Floor function $\lfloor x \rfloor$ (rounds down).

---

# 7. String Methods

Strings in Python are **immutable** (they cannot be modified in place; string methods return new strings).

```python
text = "  python programming  "
text.strip()        # Removes surrounding whitespace -> "python programming"
text.upper()        # Converts to uppercase -> "  PYTHON PROGRAMMING  "
text.title()        # Converts to Title Case -> "  Python Programming  "
text.find("p")      # Finds lowest index -> 2
text.count("m")     # Counts occurrences -> 2
text.replace(" ", "")# Replaces matching substrings
```

---

# 8. String Indexing and Slicing

Sequences support slice syntax `sequence[start : stop : step]`.

```text
 Index (Positive):   0   1   2   3   4   5
 Character:          P   Y   T   H   O   N
 Index (Negative):  -6  -5  -4  -3  -2  -1
```

- `s[0]`: First element (`'P'`).
- `s[-1]`: Last element (`'N'`).
- `s[0:4]`: Slices from index 0 up to (not including) 4 (`'PYTH'`).
- `s[::2]`: Every 2nd element (`'PTO'`).
- `s[::-1]`: Reverses the sequence (`'NOHTYP'`).

---

# 9. Format Specifiers (f-strings)

Formatted string literals (`f"..."`) allow embedding expressions with formatting specifiers `{value:flags}`:

```python
pi = 3.1415926
balance = 12500.5

f"{pi:.2f}"        # Fixed-point precision -> '3.14'
f"{balance:,.2f}"  # Thousands separator  -> '12,500.50'
f"{42:05d}"        # Zero-padded integer  -> '00042'
f"{'Title':^20}"   # Centered in 20 chars -> '       Title        '
```

---

# 10. Key Takeaways

1. **Variables are references:** Variables hold pointers to objects in heap memory.
2. **Strings are immutable:** All modification methods return a new string.
3. **Division differences:** `/` always produces a `float`, while `//` produces the integer floor.
4. **Zero-based indexing:** Slices are inclusive of `start` and exclusive of `stop` (`[start, stop)`).
