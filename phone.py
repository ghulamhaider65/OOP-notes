"""Phone subclass showing inheritance and extra state."""

from item import item


class phone(item):
    """A phone is a specialized item with `broken_phones` count."""
    
    def __init__(self, name: str, price: float, quantity = 0, broken_phones = 0):
        # Use super() to initialize common item fields
        super().__init__(name, price, quantity)
        
        # Extra validation for the new attribute on this subclass
        assert broken_phones >= 0, (
            f"broken phones {broken_phones} is not greater than or equal to zero"
        )

        # New attribute unique to phones
        self.broken_phones = broken_phones


# Example instance created at import time (for quick experiments)
phone1 =  phone("jscphonev10", 500, 5)
# print(item.all)
# print(phone.all)