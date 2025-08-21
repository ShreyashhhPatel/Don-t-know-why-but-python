
# Python Revision Handbook (Basics → Advanced, 2025-08-21)

This handbook is a fast but thorough **revision from `print()` to decorators (`@`)** and other advanced features. Each section has **examples** and **practice exercises** with **expected outputs**.

> Target version: Python 3.10+ (notes for 3.12–3.13 included).

---

## Table of Contents
1. [Printing & I/O](#1-printing--io)  
2. [Variables & Built-in Types](#2-variables--built-in-types)  
3. [Operators (incl. `:=` Walrus)](#3-operators-incl--walrus)  
4. [Control Flow & Pattern Matching (`match`)](#4-control-flow--pattern-matching-match)  
5. [Collections & Comprehensions](#5-collections--comprehensions)  
6. [Functions & Parameters](#6-functions--parameters)  
7. [Scopes, Closures, and First-Class Functions](#7-scopes-closures-and-first-class-functions)  
8. [Decorators & Wrappers (`@`)](#8-decorators--wrappers-)  
9. [Iterables, Iterators, Generators](#9-iterables-iterators-generators)  
10. [Errors & Exceptions](#10-errors--exceptions)  
11. [Context Managers](#11-context-managers)  
12. [Modules, Packages & Environments](#12-modules-packages--environments)  
13. [Object-Oriented Python](#13-object-oriented-python)  
14. [Typing & Modern Type System](#14-typing--modern-type-system)  
15. [Async & Concurrency](#15-async--concurrency)  
16. [Files & Serialization](#16-files--serialization)  
17. [Testing, Tooling & Style](#17-testing-tooling--style)  
18. [Performance Notes & GIL](#18-performance-notes--gil)  
19. [Idioms & Gotchas](#19-idioms--gotchas)  

---

## 1) Printing & I/O

**Essentials**
```py
print("Hello", 42, sep=" | ", end="\n")
name = input("Your name? ")  # str
print(f"Hi, {name!r}")       # !r uses repr()
```

**Formatting**
```py
pi = 3.14159
print(f"{pi:.2f}")         # 3.14
print("{:>6}".format(7))   # '     7'
```

**Practice**
1. Ask for a float radius and print **area of circle** with **2 decimals**.  
   _Expected_: `Area: 12.57` (for r=2).

---

## 2) Variables & Built-in Types

- Immutable: `int`, `float`, `bool`, `str`, `tuple`, `frozenset`
- Mutable: `list`, `dict`, `set`, `bytearray`
- Casting: `int("7")`, `float("2.3")`, `str(123)`

```py
s = "python"
print(s[0], s[-1], s[1:4], s[::-1])  # p n yth nohtyp
```

**Practice**
1. Given `s = "abracadabra"`, print a dict of letter -> count.  
   _Expected_: `{'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}` (order may vary).

---

## 3) Operators (incl. `:=` Walrus)

```py
x = 10
x += 3                     # 13
if (n := len("python")) > 3:
    print(n)               # 6
```

- Identity: `is`, Membership: `in`
- Chaining: `0 < x < 10`
- Truthiness: empty = False, non-empty = True

**Practice**
1. Read a line; **while** it's non-empty, print its **length** using `:=` and prompt again.  
   _Expected_: prints lengths until blank line.

---

## 4) Control Flow & Pattern Matching (`match`)

```py
def http_status(code: int) -> str:
    match code:
        case 200 | 201: return "OK-ish"
        case 400: return "Bad Request"
        case 404: return "Not Found"
        case _ if 500 <= code < 600: return "Server Error"
        case _: return "Unknown"
```
**Practice**
1. Use `match` to classify a tuple `(x, y)` as `"origin"`, `"x-axis"`, `"y-axis"`, or `"quadrant"`.  
   _Expected_: (0,0)→origin; (0,5)→y-axis; etc.

---

## 5) Collections & Comprehensions

```py
nums = [1,2,3,4]
squares = [n*n for n in nums if n % 2 == 0]  # [4,16]
d = {c: ord(c) for c in "abc"}               # {'a':97,...}
```

`collections`: `Counter`, `defaultdict`, `deque`, `namedtuple`  
`heapq`, `bisect` for algorithms.

**Practice**
1. From a list of words, build a dict `{length: count}`.  
   _Expected_: For `["a","bb","bb","ccc"]` → `{1:1, 2:2, 3:1}`.

---

## 6) Functions & Parameters

```py
def f(a, b=0, *args, c=1, **kwargs):  # positional, defaults, varargs, kw-only
    return a + b + c + sum(args) + kwargs.get("bonus", 0)

def area_rect(w: float, h: float) -> float:  # annotations
    return w*h

def only_positional(a, /, b):      ...  # `/` => a is positional-only
def only_keyword(*, k1, k2=0):     ...  # `*` => keyword-only
```

**Practice**
1. Write `mean(*nums)` that ignores non-numerics using `isinstance`.  
   _Expected_: `mean(1, "x", 3) == 2.0`.

---

## 7) Scopes, Closures, and First-Class Functions

```py
x = 1
def outer():
    x = 2
    def inner():
        nonlocal x
        x += 1
        return x
    return inner

inc = outer()
print(inc(), inc())  # 3 4
```

**Practice**
1. Create `make_counter(start=0)` returning a function that increments and returns the count.  
   _Expected_: successive calls: 1,2,3,... (from start).

---

## 8) Decorators & Wrappers (@)

**Rule 1:** Always use `functools.wraps` to preserve metadata.

```py
from functools import wraps
def timer(fn):
    @wraps(fn)
    def wrapper(*a, **kw):
        import time; t0 = time.perf_counter()
        try:
            return fn(*a, **kw)
        finally:
            dt = time.perf_counter() - t0
            print(f"{fn.__name__} took {dt:.3f}s")
    return wrapper
```

**Parameterized decorator**
```py
def retry(times=3, exceptions=(Exception,)):
    def deco(fn):
        @wraps(fn)
        def w(*a, **k):
            for i in range(times):
                try: return fn(*a, **k)
                except exceptions as e:
                    last = e
            raise last
        return w
    return deco
```

**Class decorator**
```py
def add_repr(cls):
    cls.__repr__ = lambda self: f"{cls.__name__}({self.__dict__})"
    return cls
```

**Practice**
1. Write `@once` so the function runs only on first call; later calls return the first result.  
2. Write `@debug` to log arguments and result of a function.  
   _Expected_: prints like `add(2,3) -> 5`.

---

## 9) Iterables, Iterators, Generators

```py
def gen():
    yield 1
    yield from (2,3)
for x in gen(): pass
```

`itertools`: `count`, `cycle`, `chain`, `groupby`, `accumulate`.

**Practice**
1. Implement an infinite Fibonacci generator and print first 10 values.  
   _Expected_: 0,1,1,2,3,5,8,13,21,34

---

## 10) Errors & Exceptions

```py
try:
    risky()
except ValueError as e:
    raise RuntimeError("wrap") from e
else:
    print("no error")
finally:
    cleanup()
```

**Practice**
1. Define a custom exception `NegativeError` and raise it if input < 0.  
   _Expected_: raises for -3, passes for 5.

---

## 11) Context Managers

```py
from contextlib import contextmanager

@contextmanager
def open_upper(path):
    f = open(path)
    try:
        yield (line.upper() for line in f)
    finally:
        f.close()
```

**Practice**
1. Build a context manager that **changes CWD** inside the block then restores it.  
   _Expected_: after `with`, `os.getcwd()` is back to original.

---

## 12) Modules, Packages & Environments

- `import x as y`, `from pkg import mod`
- Package = folder with `__init__.py`
- Entry point: `if __name__ == "__main__":`
- Virtual env: `python -m venv .venv` → `pip install -U pip`

**Practice**
1. Create a package `mathx` with `area.py` exposing `circle(r)` and `rect(w,h)`.  
   _Expected_: `from mathx.area import circle` works.

---

## 13) Object-Oriented Python

```py
from dataclasses import dataclass

@dataclass(slots=True)
class Point:
    x: float; y: float
    def __add__(self, other): return Point(self.x+other.x, self.y+other.y)
```

- `@property`, `@classmethod`, `@staticmethod`
- Inheritance & MRO, `super()`
- `abc.ABC`, `@abstractmethod`
- Protocols (duck typing with `typing.Protocol`)

**Practice**
1. Create an abstract `Shape.area()`; implement `Circle` & `Rect`.  
   _Expected_: correct areas; `Shape()` cannot be instantiated.

---

## 14) Typing & Modern Type System

```py
from typing import Iterable, Protocol, TypeVar, Optional, overload
T = TypeVar("T")
def first(xs: Iterable[T]) -> Optional[T]: ...
```

**Generics (3.12):**
```py
def pair[T](a: T, b: T) -> tuple[T, T]:
    return (a, b)
```

**@override (3.12):**
```py
from typing import override
class Base:  def ping(self) -> str: return "base"
class Child(Base):
    @override
    def ping(self) -> str: return "child"
```

**Practice**
1. Write a `Protocol` `SupportsArea` with `.area()->float` and a function that accepts any such object.  
   _Expected_: Works for both `Circle` and `Rect` without inheritance.

---

## 15) Async & Concurrency

- `threading` (I/O-bound), `multiprocessing` (CPU-bound), `asyncio` (high-concurrency I/O)
```py
import asyncio, aiohttp  # third-party
async def fetch(url):
    async with aiohttp.ClientSession() as s:
        async with s.get(url) as r:
            return await r.text()
asyncio.run(fetch("https://example.com"))
```

**Practice**
1. Use `asyncio.gather` to fetch 3 URLs concurrently (mock with `asyncio.sleep`).  
   _Expected_: roughly the max sleep time, not sum.

---

## 16) Files & Serialization

```py
from pathlib import Path
p = Path("data.txt"); p.write_text("hello\n")
print(p.read_text())
import json
print(json.dumps({"a":1}))
```

**Practice**
1. Convert CSV (name,score) to JSON list of dicts.  
   _Expected_: `[{{"name":"A","score":10}}, ...]`.

---

## 17) Testing, Tooling & Style

- `pytest -q`, `unittest`
- Formatters/linters: `black`, `ruff`
- Pre-commit hooks

**Practice**
1. Write tests for your `once` and `retry` decorators.  
   _Expected_: tests pass; retries happen thrice.

---

## 18) Performance Notes & GIL

- Profile: `python -m cProfile -o out.prof your_script.py`, inspect with `snakeviz`.
- Vectorize with `numpy` when heavy loops.
- Understand GIL: threads don't run Python bytecode truly in parallel for CPU-bound tasks; use `multiprocessing` or C-extensions.

**Practice**
1. Benchmark list comprehension vs. generator + `sum` with `timeit`.  
   _Expected_: list comp often faster for modest sizes.

---

## 19) Idioms & Gotchas

- EAFP > LBYL: try/except instead of pre-checks
- Mutable default args pitfall: use `None` then assign
```py
def f(b=None):
    if b is None: b = []
```
- Prefer `pathlib` over raw paths; `enumerate`, `zip`, `dict.get`, `with` blocks

---

### Mini-Quiz (10 quick checks)

1. What does `@wraps` preserve?  
2. Difference between `is` and `==`?  
3. When use `match` vs `if/elif`?  
4. What does `/` in def parameter list do?  
5. Show a keyword-only argument example.  
6. How to make a class read-only point (`x,y`) and memory-efficient?  
7. What is a generator vs an iterator?  
8. When to use `multiprocessing` over `threading`?  
9. One use-case for `Protocol`?  
10. One-liner to count letters in a string?

**Suggested answers**:  
1. name, docstring, module, annotations (metadata).  
2. Identity vs equality.  
3. Complex shape-matching on structured data.  
4. Forces positional-only params.  
5. Use `*` to separate: `def f(*, k): ...`.  
6. `@dataclass(slots=True, frozen=True)`.  
7. Iterator: has `__iter__` & `__next__`; generator: function using `yield` that creates an iterator.  
8. CPU-bound tasks.  
9. Static duck-typing without inheritance.  
10. `collections.Counter(s)`.

---

Happy revising! Save this file and run snippets in a REPL or notebook.
