# Python Fundamentals — Lesson 3: Loops & Iteration

> **Goal:** Master iteration mechanics in Python: while loops, sentinel loops, for loops with ranges, loop control statements (`break`, `continue`, `else`), nested loops, and the iterable protocol.

---

# Table of Contents
1. [Loop Architectures in Python](#1-loop-architectures-in-python)
2. [While Loops & Input Validation](#2-while-loops--input-validation)
3. [Sentinel Loops](#3-sentinel-loops)
4. [For Loops and the `range()` Function](#4-for-loops-and-the-range-function)
5. [Loop Control: `break`, `continue`, and `pass`](#5-loop-control-break-continue-and-pass)
6. [Nested Loops and Multidimensional Traversal](#6-nested-loops-and-multidimensional-traversal)
7. [The Python Iteration Protocol](#7-the-python-iteration-protocol)
8. [Common Pitfalls & Best Practices](#8-common-pitfalls--best-practices)
9. [Key Takeaways](#9-key-takeaways)

---

# 1. Loop Architectures in Python

Python provides two primary looping constructs:
- **`while` loop:** Condition-controlled iteration. Repeats indefinitely as long as a boolean expression evaluates to `True`.
- **`for` loop:** Collection-controlled iteration. Iterates over elements of an iterable sequence until exhaustion.

```text
┌─────────────────────────────────┐       ┌─────────────────────────────────┐
│           While Loop            │       │            For Loop             │
├─────────────────────────────────┤       ├─────────────────────────────────┤
│ Condition -> True -> Run Body   │       │ Pull Next Item from Iterable    │
│ Condition -> False -> Terminate │       │ No more items -> Terminate      │
└─────────────────────────────────┘       └─────────────────────────────────┘
```

---

# 2. While Loops & Input Validation

While loops are the standard pattern for sanitizing and validating dynamic user input:

```python
age = int(input("Enter age: "))
while age < 0:
    print("Invalid age!")
    age = int(input("Enter age: "))
```

---

# 3. Sentinel Loops

A sentinel value is a predefined marker (e.g. `'q'`, `-1`) that instructs the loop to finish collecting input:

```python
food = input("Enter food (q to quit): ")
while food.lower() != "q":
    # Process item
    food = input("Enter food (q to quit): ")
```

---

# 4. For Loops and the `range()` Function

`range(start, stop[, step])` generates integers lazily on demand without allocating entire lists in memory.

| Call | Sequence Produced |
| :--- | :--- |
| `range(5)` | `0, 1, 2, 3, 4` |
| `range(1, 6)` | `1, 2, 3, 4, 5` |
| `range(0, 10, 2)` | `0, 2, 4, 6, 8` |
| `range(5, 0, -1)` | `5, 4, 3, 2, 1` |

---

# 5. Loop Control: `break`, `continue`, and `pass`

- `break`: Immediately exits the innermost enclosing loop.
- `continue`: Skips the remainder of the current iteration and jumps to the next cycle.
- `pass`: Syntactic no-op placeholder.

```python
for num in range(1, 20):
    if num % 2 == 0:
        continue  # Skip even numbers
    if num > 10:
        break     # Stop once numbers exceed 10
    print(num)
```

---

# 6. Nested Loops and Multidimensional Traversal

Outer loops dictate row-level transitions; inner loops dictate column-level execution:

```text
Outer Loop (Row 0) ──> Inner Loop (Col 0 -> Col 1 -> Col 2)
Outer Loop (Row 1) ──> Inner Loop (Col 0 -> Col 1 -> Col 2)
Outer Loop (Row 2) ──> Inner Loop (Col 0 -> Col 1 -> Col 2)
```

Time complexity for an $M \times N$ matrix iteration is $O(M \cdot N)$.

---

# 7. The Python Iteration Protocol

Any object implementing `__iter__()` and `__next__()` can be looped over with `for`:
- Lists, Tuples, Sets, Dictionaries, Strings, Files, Generators.

When iterating dictionaries:
- `for k in dict:` -> Iterates **keys**
- `for v in dict.values():` -> Iterates **values**
- `for k, v in dict.items():` -> Iterates **(key, value) pairs**

---

# 8. Common Pitfalls & Best Practices

1. **Infinite While Loops:** Always ensure the loop condition variable is modified inside the body.
2. **Modifying Sequences While Iterating:** Never mutate (add/remove from) a `list` while iterating directly over it; iterate over a slice copy `list[:]` instead.
3. **Use `enumerate()` for Indexing:** Prefer `for idx, item in enumerate(items):` over manual counters.

---

# 9. Key Takeaways

1. Use `for` loops when the iteration count or collection length is known; use `while` loops when looping depends on dynamic conditions.
2. `range()` is memory-efficient because it computes values on demand in $O(1)$ memory.
3. `break` and `continue` provide precise control over loop execution paths.
