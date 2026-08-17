# Python Fundamentals — Lesson 5: Functions, Arguments & Scope

> **Goal:** Build robust, reusable subroutines. Master parameter passing models, default values, `*args`, `**kwargs`, and Python's LEGB variable resolution rules.

---

# Table of Contents
1. [Function Anatomy and Call Mechanics](#1-function-anatomy-and-call-mechanics)
2. [Positional vs. Keyword Arguments](#2-positional-vs-keyword-arguments)
3. [Default Arguments & Mutable Defaults Gotcha](#3-default-arguments--mutable-defaults-gotcha)
4. [Variable Arguments (`*args` and `**kwargs`)](#4-variable-arguments-args-and-kwargs)
5. [The LEGB Scope Rule](#5-the-legb-scope-rule)
6. [Key Takeaways](#6-key-takeaways)

---

# 1. Function Anatomy and Call Mechanics

Functions encapsulate repeatable algorithms:

```python
def function_name(param1: type, param2: type = default) -> return_type:
    """Docstring explaining purpose, inputs, and outputs."""
    # Function body
    return result
```

When a function executes, Python pushes a new stack frame containing local variables onto the call stack, popping it upon returning.

---

# 2. Positional vs. Keyword Arguments

- **Positional:** Bound strictly by index order.
- **Keyword:** Explicitly named in the call `func(param=val)`; order is arbitrary.

```python
def greet(first, last):
    print(f"Hello, {first} {last}!")

greet("Dexter", "Morgan")              # Positional
greet(last="Morgan", first="Dexter")    # Keyword
```

---

# 3. Default Arguments & Mutable Defaults Gotcha

> [!WARNING]
> Default parameter expressions are evaluated **once at function definition time**, NOT each time the function is called!
> Never use mutable defaults (e.g. `def append_to(item, target=[])`). Use `target=None` and initialize inside the body.

```python
# CORRECT PATTERN:
def append_to(item, target=None):
    if target is None:
        target = []
    target.append(item)
    return target
```

---

# 4. Variable Arguments (`*args` and `**kwargs`)

```text
def func(*args, **kwargs):
           │         │
           ▼         ▼
       (tuple)    {dict}
```

- `*args`: Collects extra positional parameters as a `tuple`.
- `**kwargs`: Collects extra keyword arguments as a `dict`.

---

# 5. The LEGB Scope Rule

Python resolves identifiers hierarchically using the **LEGB** search sequence:

```text
┌───────────────────────────────────────────────┐
│ Local (L): Variables inside current function  │
└───────────────────────┬───────────────────────┘
                        ▼
┌───────────────────────────────────────────────┐
│ Enclosing (E): Variables in outer functions   │
└───────────────────────┬───────────────────────┘
                        ▼
┌───────────────────────────────────────────────┐
│ Global (G): Module top-level variables        │
└───────────────────────┬───────────────────────┘
                        ▼
┌───────────────────────────────────────────────┐
│ Built-in (B): Pre-assigned names (len, print) │
└───────────────────────────────────────────────┘
```

---

# 6. Key Takeaways

1. **Functions reduce duplication** and provide clear abstractions.
2. **`*args` and `**kwargs`** allow writing highly flexible, variadic interfaces.
3. **LEGB rule** dictates variable visibility; avoid polluting global state by keeping variables local.
