# Python Fundamentals — Lesson 2: Conditionals & Logic

> **Goal:** Understand control flow mechanisms, short-circuit boolean evaluation, ternary operators, and membership checks across Python sequences and mappings.

---

# Table of Contents
1. [Conditional Execution Flow](#1-conditional-execution-flow)
2. [Comparison Operators](#2-comparison-operators)
3. [Logical Operators and Short-Circuiting](#3-logical-operators-and-short-circuiting)
4. [Ternary Conditional Expressions](#4-ternary-conditional-expressions)
5. [Membership Operators (`in` and `not in`)](#5-membership-operators-in-and-not-in)
6. [Common Pitfalls & Best Practices](#6-common-pitfalls--best-practices)
7. [Key Takeaways](#7-key-takeaways)

---

# 1. Conditional Execution Flow

Control flow alters linear execution based on runtime conditions:

```text
               ┌───────────────┐
               │   Condition   │
               └───────┬───────┘
                       │
             True ┌────┴────┐ False
                  ▼         ▼
             ┌─────────┐ ┌─────────┐
             │ If Body │ │Elif/Else│
             └────┬────┘ └────┬────┘
                  │           │
                  └─────┬─────┘
                        ▼
               ┌─────────────────┐
               │ Next Statement  │
               └─────────────────┘
```

```python
if condition_1:
    # Executes only if condition_1 is True
elif condition_2:
    # Executes if condition_1 is False AND condition_2 is True
else:
    # Executes if all preceding conditions are False
```

---

# 2. Comparison Operators

| Operator | Meaning | Example |
| :--- | :--- | :--- |
| `==` | Value equality | `5 == 5` (`True`) |
| `!=` | Value inequality | `5 != 3` (`True`) |
| `<` / `>` | Less than / Greater than | `3 < 7` (`True`) |
| `<=` / `>=` | Less/Greater or equal | `10 >= 10` (`True`) |
| `is` | Identity (same memory address) | `a is None` |

> **Note:** Chained comparisons are valid and concise in Python: `0 < temp <= 30` is equivalent to `(0 < temp) and (temp <= 30)`.

---

# 3. Logical Operators and Short-Circuiting

Python provides three boolean operators:
- `and`: Evaluates to `True` only if **both** operands are truthy.
- `or`: Evaluates to `True` if **at least one** operand is truthy.
- `not`: Unary negation.

### Short-Circuit Evaluation:
- For `A and B`: If `A` is `False`, Python immediately returns `A` without evaluating `B`.
- For `A or B`: If `A` is `True`, Python immediately returns `A` without evaluating `B`.

```python
# Safe guard against division by zero using short-circuiting:
if count != 0 and (total / count) > threshold:
    print("Threshold met!")
```

---

# 4. Ternary Conditional Expressions

A concise one-line syntax for simple conditional value assignment:

```text
Result = [Value if True] if [Condition] else [Value if False]
```

```python
parity = "EVEN" if n % 2 == 0 else "ODD"
status = "Adult" if age >= 18 else "Minor"
```

---

# 5. Membership Operators (`in` and `not in`)

Membership operators test whether a target exists inside a container:

| Target Type | Target Container | Time Complexity | Notes |
| :--- | :--- | :--- | :--- |
| Character / Substring | `str` | $O(N)$ | Case-sensitive substring search |
| Element | `list` / `tuple` | $O(N)$ | Linear search through elements |
| Element | `set` | $O(1)$ avg | Instant hash table lookup |
| Key | `dict` | $O(1)$ avg | Checks **keys** by default |

```python
# Checking dictionary keys:
if "Dexter" in grade_book:
    print(grade_book["Dexter"])

# Checking dictionary values:
if "A+" in grade_book.values():
    print("Top honor awarded!")
```

---

# 6. Common Pitfalls & Best Practices

1. **`==` vs `is`:** Use `==` to compare **values** (`a == 5`), but use `is` to check singletons like `None` (`x is None` or `x is not None`).
2. **Implicit Truthiness:** Prefer `if items:` over `if len(items) > 0:` for checking empty sequences.
3. **Avoid Deep Nesting:** Invert conditions and use early returns or `elif` ladders to reduce cognitive complexity ("arrow anti-pattern").

---

# 7. Key Takeaways

1. **Short-circuiting saves CPU and prevents errors:** Second operands are evaluated lazily.
2. **Membership operators simplify search logic:** Use `item in set_collection` for instant $O(1)$ checks.
3. **Ternary expressions keep code clean:** Use them for straightforward assignments, but avoid nesting them.
