# Python OOP Notes — Complete, Practical, and Simple

Use this repo to learn and revise Object-Oriented Programming (OOP) in Python using small, focused examples. The code is intentionally simple, heavily commented, and ready to run.

What’s inside (files map to concepts)
- `class.py` — Your first class: methods and instance attributes
- `item.py` — Core OOP ideas: encapsulation, properties, class/instance attributes, classmethod, staticmethod, dunder `__repr__`
- `phone.py` — Inheritance with an extra attribute (`broken_phones`)
- `keyboard.py` — Simple inheritance with no new attributes
- `polymor.py` — Polymorphism demo using the same function on different types
- `main.py` — Tiny entry point to try the classes quickly
- `items.csv` — Sample data for the CSV constructor in `item.py`
- `abstraction.py` — Abstraction with an abstract base class and two implementations- `fraction.py` — Basic Fraction class with `__str__` dunder method for custom string representation
- `xyz.py` — Interactive ATM system demo with menu-driven operations (PIN, deposit, withdraw, balance check)
How to use these notes
1) Open each file and read the comments/docstrings.
2) Run `main.py` to see a quick demo.
3) Try the optional exercises at the end to practice.

Key OOP concepts explained
1) Class vs Instance
- Class: a blueprint that defines data and behavior (e.g., `class item:`).
- Instance: a concrete object created from the class (e.g., `p = item(...)`).

2) Encapsulation (hiding internal details)
- In `item.py`, `__name` and `__price` are private. Access them via properties.
- Why: keeps objects valid and prevents accidental misuse.

3) Properties (getters/setters in Python style)
- `@property` exposes read access; `@name.setter` validates and updates safely.
- Example: `item.name` is limited to a max length; invalid values raise errors.

4) Class vs Instance attributes
- Class attributes are shared: `item.pay_rate` and `item.all` (a registry list).
- Instance attributes are unique per object: e.g., `quantity`.

5) Methods you should know
- Instance methods: operate on one object (`calculate_total_price`).
- Class methods (`@classmethod`): alternate constructors like `instantiate_from_csv()`.
- Static methods (`@staticmethod`): utility functions like `is_integer()`.

6) Inheritance
- `phone(item)`: adds `broken_phones` while reusing base logic.
- `keybord(item)`: inherits behavior without adding new fields.

7) Dunder (special) methods
- `__repr__`: returns a helpful string for debugging and printing lists of objects.

8) Polymorphism
- Built-in example: `len()` works on strings and lists (`polymor.py`).
- Idea: code that works with different types as long as they support the needed behavior.

Where to find each pillar in code
- Abstraction: `abstraction.py` (Notifier ABC), `item.py` (`send_email` hides internals)
- Encapsulation: `item.py` (private `__price`, `__name`, properties)
- Inheritance: `phone.py`, `keyboard.py` (both extend `item`)
- Polymorphism: `polymor.py` and `abstraction.py` (same interface, different behavior)

Quick start (run these)
- Run the tiny demo:
	- python main.py
- Load items from CSV (uncomment in `main.py`):
	- item.instantiate_from_csv()
	- print(item.all)

Reading guide per file
- `class.py`: Minimal class to see how methods and instance attributes stick together.
- `item.py`: The “full” example. Read its comments to understand:
	- Why we use private attributes and properties.
	- How class attributes differ from instance attributes.
	- How `@classmethod` implements an alternate constructor from a CSV file.
	- How `@staticmethod` provides a utility that doesn’t depend on one object.
	- Why `__repr__` is useful during debugging.
- `phone.py`: Shows how a subclass adds a new attribute and validates it.
- `keyboard.py`: Inherits everything from `item` as-is.
- `polymor.py`: Demonstrates polymorphism with a built-in function.- `fraction.py`: Simple class showing `__str__` dunder method for custom object representation.
- `xyz.py`: Practical ATM application demonstrating:
	- Constructor initialization with default values.
	- User input handling and menu-driven interface.
	- Instance methods working together (create_pin, deposit, withdraw, check_balance).
	- Control flow with while loop and conditional statements.
Practice (short exercises)
- Add a new subclass `mouse(item)` with a `dpi` attribute and basic validation.
- In `item.py`, add a method `increase_stock(n)` to add to `quantity` (n must be >= 0).
- Extend `polymor.py` with your own function that works on any object having a method `export()` (duck typing idea).

FAQ
- Why are class names lowercase like `item`? The original project used this style; we kept it to match your code. In production code, classes are usually `CamelCase` like `Item`.
- Why private attributes (`__price`)? To prevent direct modification and centralize validation.
- Why use `__repr__`? It makes interactive sessions and logs much easier to read.

Tip
- Read top-to-bottom, run small experiments, and keep notes directly in comments. The goal is clarity, not complexity.