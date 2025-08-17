"""Keyboard subclass example showing simple inheritance."""

from item import item


class keybord(item):
    """A keyboard is a kind of item — no extra fields yet.

    Note: Class name kept as `keybord` to match your original code.
    """

    def __init__(self, name: str, price: float, quantity = 0):
        # Call to super() to reuse parent's initialization/validation
        super().__init__(name, price, quantity)
        