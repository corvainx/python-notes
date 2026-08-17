# Python Fundamentals — Lesson 8: Modules & Advanced Python

> **Goal:** Master modular project composition, the `__name__ == '__main__'` entry point idiom, robust error handling hierarchies, date/time operations, and HTTP network requests.

---

# Table of Contents
1. [Python Module Resolution System](#1-python-module-resolution-system)
2. [The `if __name__ == '__main__':` Guard](#2-the-if-__name__--__main__-guard)
3. [Exception Hierarchy & Defensive Programming](#3-exception-hierarchy--defensive-programming)
4. [Date & Time Management (`datetime`)](#4-date--time-management-datetime)
5. [Consuming REST APIs over HTTP](#5-consuming-rest-apis-over-http)
6. [Key Takeaways](#6-key-takeaways)

---

# 1. Python Module Resolution System

When executing `import my_module`, Python searches across paths in `sys.path`:

```text
1. Directory of the input script (or current working directory)
2. PYTHONPATH environment variable entries
3. Standard library directories
4. Installed site-packages (pip dependencies)
```

---

# 2. The `if __name__ == '__main__':` Guard

Every Python file has a special built-in variable `__name__`:
- If executed directly: `__name__ = "__main__"`
- If imported by another file: `__name__ = "module_filename"`

```python
def solve():
    print("Algorithm executed.")

if __name__ == "__main__":
    # Test suite or CLI runner; won't execute on import
    solve()
```

---

# 3. Exception Hierarchy & Defensive Programming

```text
               BaseException
                     │
                 Exception
         ┌───────────┼──────────────┬─────────────┐
         ▼           ▼              ▼             ▼
   ArithmeticError  LookupError   TypeError    ValueError
     (ZeroDiv)      (Key/Index)
```

### Complete `try-except-else-finally` Lifecycle:
- `try`: Code that might raise an error.
- `except ExceptionType as err`: Handles specific error types.
- `else`: Runs **only** if no exceptions were raised.
- `finally`: Guarantees cleanup execution (closing sockets, freeing locks).

---

# 4. Date & Time Management (`datetime`)

- `datetime.date`: Calendar year, month, day.
- `datetime.time`: Hours, minutes, seconds, microseconds.
- `datetime.datetime`: Combined date and time timestamp.
- `datetime.timedelta`: Duration between two date/time points.
- `strftime()`: Formats datetime objects into customized strings.
- `strptime()`: Parses strings into datetime objects.

---

# 5. Consuming REST APIs over HTTP

Web communication utilizes standard REST endpoints over HTTP/HTTPS:
- Check HTTP status codes (`200 OK`, `404 Not Found`, `500 Server Error`).
- Parse JSON payloads with `json.loads()`.
- Implement defensive timeouts to prevent hanging processes.

---

# 6. Key Takeaways

1. **Always use `if __name__ == '__main__':`** in executable scripts to enable clean reusability as imported libraries.
2. **Never catch bare `except:`**; always catch specific exceptions (`ValueError`, `FileNotFoundError`) to avoid masking critical system signals like `KeyboardInterrupt`.
3. **Use `try/except/else/finally`** for rigorous, deterministic resource lifecycles.
