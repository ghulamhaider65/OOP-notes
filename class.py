"""Simplest class example to show how data and behavior live together."""


class item:
    # A method is a function defined inside a class.
    # `self` is the instance (the specific object) the method is called on.
    def calculate_total_price(self, x, y):
        return x * y


# Create two different objects (instances) of the same class
item1 = item()
item1.name = "phone"   # adding attributes on the instance
item1.price = 100
item1.quantity = 5
print(item1.calculate_total_price(item1.price, item1.quantity))

item2 = item()
item2.name = "laptop"
item2.price = 1000
item2.quantity = 3
print(item2.calculate_total_price(item2.price, item2.quantity))

