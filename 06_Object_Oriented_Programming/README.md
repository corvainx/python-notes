# Python Fundamentals — Lesson 6: Object-Oriented Programming (OOP)

> **Goal:** Master OOP paradigms in Python: encapsulation, abstraction, inheritance hierarchies, polymorphism, method resolution order (MRO), dunder magic methods, and property decorators.

---

# Table of Contents
1. [Core Pillars of Object-Oriented Design](#1-core-pillars-of-object-oriented-design)
2. [Class Anatomy: Instance vs. Class Variables](#2-class-anatomy-instance-vs-class-variables)
3. [Inheritance and the `super()` Dispatcher](#3-inheritance-and-the-super-dispatcher)
4. [Abstract Base Classes (`abc` module)](#4-abstract-base-classes-abc-module)
5. [Polymorphism & Duck Typing](#5-polymorphism--duck-typing)
6. [Static Methods & Class Methods](#6-static-methods--class-methods)
7. [Relationship Modeling: Aggregation vs. Composition](#7-relationship-modeling-aggregation-vs-composition)
8. [Data Encapsulation & `@property` Descriptors](#8-data-encapsulation--property-descriptors)
9. [Operator Overloading & Dunder Methods](#9-operator-overloading--dunder-methods)
10. [Key Takeaways](#10-key-takeaways)

---

# 1. Core Pillars of Object-Oriented Design

```text
               ┌────────────────────────────────────────────────────────┐
               │              Four Pillars of OOP in Python             │
               └───────────────────────────┬────────────────────────────┘
         ┌──────────────────┬──────────────┴─────┬──────────────────┐
         ▼                  ▼                    ▼                  ▼
  Encapsulation        Abstraction          Inheritance        Polymorphism
 (Data Hiding &       (Enforcing Core      (Code Reuse via     (Multiple Types,
  Access Control)       Contracts)         Base Classes)       Single Interface)
```

---

# 2. Class Anatomy: Instance vs. Class Variables

- **Instance Variables (`self.var`):** Distinct per instantiated object.
- **Class Variables (`ClassName.var`):** Stored once in the class object namespace; shared by all instances.

---

# 3. Inheritance and the `super()` Dispatcher

`super()` allows calling parent implementations without hardcoding parent class names, adhering to the C3 Linearization Method Resolution Order (MRO):

```python
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
```

---

# 4. Abstract Base Classes (`abc` module)

Abstract base classes define strict interface contracts that child classes must implement:

```python
from abc import ABC, abstractmethod

class Plugin(ABC):
    @abstractmethod
    def execute(self):
        pass
```

Attempting to instantiate a class missing abstract method implementations raises `TypeError`.

---

# 5. Polymorphism & Duck Typing

Python adheres to dynamic typing / duck typing:
> *"If it walks like a duck and quacks like a duck, it's a duck."*

Explicit inheritance is not required as long as objects expose matching method signatures.

---

# 6. Static Methods & Class Methods

| Decorator | First Argument | Purpose |
| :--- | :--- | :--- |
| *(None / standard)* | `self` (instance) | Operates on individual instance attributes |
| `@classmethod` | `cls` (class) | Operates on class state; alternative constructors |
| `@staticmethod` | *(None)* | Utility function living in class namespace |

---

# 7. Relationship Modeling: Aggregation vs. Composition

```text
Aggregation (HAS-A):   [ Library ] ──(references)──> [ Book ] (Lives independently)
Composition (PART-OF): [ Car ]     ──(owns)────────> [ Engine ] (Destroyed with Car)
```

---

# 8. Data Encapsulation & `@property` Descriptors

Use `@property` to expose getters and `@attribute.setter` to apply input validation transparently without breaking existing API signatures:

```python
@property
def radius(self):
    return self._radius

@radius.setter
def radius(self, val):
    if val <= 0:
        raise ValueError("Radius must be positive")
    self._radius = val
```

---

# 9. Operator Overloading & Dunder Methods

| Magic Method | Triggers When... | Example Usage |
| :--- | :--- | :--- |
| `__init__` | Object instantiation | `obj = MyClass()` |
| `__str__` | Converted to string for users | `print(obj)`, `str(obj)` |
| `__repr__` | Unambiguous dev representation | `repr(obj)` |
| `__eq__` | Equality check | `obj1 == obj2` |
| `__len__` | Length query | `len(obj)` |
| `__add__` | Binary addition | `obj1 + obj2` |

---

# 10. Key Takeaways

1. **Favor Composition over Inheritance** for flexible object lifecycles.
2. **Use `@property`** instead of Java-style `get_x()` and `set_x()` methods.
3. **Implement `__repr__` on every class** for vastly superior debugging experiences.
