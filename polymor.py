"""Polymorphism demo: same function works with different types.

Here, the built-in function `len()` is used with a string and a list.
It behaves correctly because both types implement a length protocol.
"""

name = "Jim"  # str
print(len(name))  # -> 3

some_list = ["Some", "Name"]  # list
print(len(some_list))  # -> 2