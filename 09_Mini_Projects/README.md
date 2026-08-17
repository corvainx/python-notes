# Python Fundamentals — Lesson 9: Mini Projects & Applications

> **Goal:** Apply Python concepts into practical, interactive command-line utilities and algorithmic mini-applications.

---

# Table of Contents
1. [Project Overview](#1-project-overview)
2. [Project Catalogue & Concepts Applied](#2-project-catalogue--concepts-applied)
3. [Running the Projects](#3-running-the-projects)
4. [Key Takeaways](#4-key-takeaways)

---

# 1. Project Overview

These 11 standalone mini-projects synthesize core language fundamentals into practical tools:

```text
┌────────────────────────────────────────────────────────┐
│                   Python Mini Projects                 │
└───────────────────────────┬────────────────────────────┘
        ┌───────────────────┼────────────────────┐
        ▼                   ▼                    ▼
Interactive Games      Math & Financial     System & Security
 (MadLibs, Guessing)  (Calculators, Prime) (Encryption, Timer)
```

---

# 2. Project Catalogue & Concepts Applied

| # | Project Script | Key Concepts Applied |
| :--- | :--- | :--- |
| 01 | `01_madlibs_game.py` | String concatenation, `input()`, f-strings |
| 02 | `02_calculator.py` | Arithmetic operators, branching logic, exception guards |
| 03 | `03_weight_converter.py` | Floating-point math, unit conversions, case handling |
| 04 | `04_temperature_converter.py` | Formulaic conversion, Celsius-Fahrenheit mappings |
| 05 | `05_compound_interest_calc.py` | While loop input validation, exponential arithmetic |
| 06 | `06_countdown_timer.py` | `time.sleep`, modular time calculation (HH:MM:SS), terminal buffer flushing |
| 07 | `07_shopping_cart.py` | Parallel lists, dynamic collection, `sum()`, string alignment |
| 08 | `08_caesar_cipher_encryption.py` | `random.shuffle`, string character mapping, cryptography basics |
| 09 | `09_number_guessing_game.py` | `random.randint`, binary search hinting, loop state tracking |
| 10 | `10_prime_number_checker.py` | Number theory, $O(\sqrt{N})$ trial division optimization |
| 11 | `11_variable_swapper.py` | Tuple unpacking, bytecode memory efficiency |

---

# 3. Running the Projects

Execute any project script directly in your terminal:

```bash
python3 09_Mini_Projects/05_compound_interest_calc.py
python3 09_Mini_Projects/08_caesar_cipher_encryption.py
```

---

# 4. Key Takeaways

1. **Defensive Input Handling:** Always wrap numerical inputs in `try/except ValueError` to prevent terminal crashes.
2. **Modular Helper Functions:** Break interactive logic into pure computational functions and I/O handlers.
3. **Format Alignment:** Use fixed-width f-string specifiers (`f"{val:>10.2f}"`) for clean terminal receipts and tabular summaries.
