# OOP Notes (Python) — Simple and Practical

This repo contains short, easy examples to understand Object-Oriented Programming (OOP) in Python.

What's inside
- `class.py`: The simplest class example (methods and instance attributes)
- `item.py`: A full example with properties, class attributes, class/staticmethods
- `phone.py`: Inheritance example that adds a new attribute
- `keyboard.py`: Simple inheritance without adding new fields
- `polymor.py`: Polymorphism demo using `len()` on different types
- `main.py`: Small script to quickly try the classes
- `items.csv`: Data used by `item.instantiate_from_csv()`

Key OOP ideas in this project
1) Class vs Instance
	- Class: a blueprint (e.g., `item`) that defines data and behavior
	- Instance: an object created from a class (e.g., `item()`, `phone()`)

2) Encapsulation
	- We hide internal details like `__price` and `__name` and expose them using
	  properties (`name`, `price`). This keeps the object valid.

3) Class attributes vs Instance attributes
	- Class attributes: shared by all objects (e.g., `pay_rate` and `all`)
	- Instance attributes: unique per object (e.g., `quantity` on each item)

4) Inheritance
	- `phone(item)`: adds `broken_phones` and reuses `item` logic
	- `keybord(item)`: reuses `item` logic without new fields

5) Class methods and Static methods
	- `@classmethod instantiate_from_csv`: alternative constructor that reads `items.csv`
	- `@staticmethod is_integer`: a helper that doesn't depend on a specific object

6) Dunder method
	- `__repr__`: returns a helpful string when you print objects or lists of them

Try it
1) Run `python main.py` and see output from a `keybord` instance.
2) Open `item.py` and read the comments/docstrings for the full explanation.
3) (Optional) Uncomment lines in `main.py` to try CSV loading and discounts.

Tip: Read the code top-to-bottom. The comments explain the “why” of each part.