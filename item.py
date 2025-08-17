"""Core OOP example: an Item class with attributes, methods, and utilities.

This file demonstrates key OOP ideas:
- Class vs instance attributes (`pay_rate`, `all` vs per-object fields)
- Encapsulation (private attributes like `__name` and `__price`)
- Properties/getters-setters (controlled access to attributes)
- Class methods (alternative constructors) and static methods (utilities)
- Special/dunder methods like `__repr__` for better printing/debugging
"""

import csv

class item:
    """Represents a generic store item.

    Note: Class name kept as `item` to match your original code.
    """

    # Class attributes (shared by all objects of this class)
    pay_rate = 0.8  # 20% discount applied by apply_discount()
    all = []  # a registry of all created items (instances)
    
    def __init__(self, name: str, price: float, quantity = 0):
        """Initialize a new item (object/instance).

        Args:
            name: The product name.
            price: Unit price (must be >= 0).
            quantity: How many we have in stock (must be >= 0).
        """


    # Validation (defensive programming): make sure inputs are valid
        assert price >= 0 , f"price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"quantity {quantity} is not greater than or equal to zero"

    # Assign to the object (self) — these are instance attributes
        self.__name = name
        self.__price = price
        self.quantity = quantity

    # Keep track of this instance at the class level
        item.all.append(self)

    @property
    def price(self):
        """Read-only property for price (encapsulation).

        We expose price via a getter so price changes go through methods
        like apply_discount/apply_increment.
        """
        return self.__price
    
    def apply_discount(self):
        """Apply the class-wide discount to the price."""
        self.__price = self.__price * item.pay_rate


    def apply_increment(self, increment_value):
        """Increase price by a percentage (e.g., 0.2 = +20%)."""
        self.__price = self.__price + self.__price * increment_value

    @property
    # Property decorator = Read only attribute
    def name(self):
        """Read the name (use the setter to update safely)."""
        return self.__name
    
    @name.setter
    def name(self, value):
        """Validate and set the name. Keeps the object in a valid state."""
        if len(value) > 10:
            raise Exception ("The name is too long")
        else:
            self.__name = value

    def calculate_total_price(self):
        """Return total inventory value for this item."""
        return self.__price * self.quantity
    

    @classmethod
    def instantiate_from_csv(cls):
        """Alternative constructor: build items from items.csv.

        Reads the CSV file into a list of dicts, then creates item objects.
        The new objects are also stored in `item.all`.
        """
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            cls(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        """Return True for ints and floats like 5.0 (no fractional part).

        Examples: 5 -> True, 5.0 -> True, 5.1 -> False
        """
        # We will count out the floats that are point zero (e.g. 5.0, 10.0)
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False


    def __repr__(self):
        """Unambiguous string representation (useful for debugging)."""
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
    
    def __connect(self, smtp_server):
        # Pretend to set up an email connection (implementation hidden)
        pass

    def __prepare_body(self):
        # Prepare a simple email body using this object's data
        return f"""
        Hello Haider.
        We have {self.name} {self.quantity} times.
        Regards,
        JimShapedCoding
        """
    
    def __send(self):
        # Pretend to send the email
        pass
    
    def send_email(self):
        """Public method: hides the email sending details from the caller."""
        self.__connect('')
        self.__prepare_body()
        self.__send()

    
