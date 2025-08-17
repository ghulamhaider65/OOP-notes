"""Entry point to try the classes quickly.

Import the classes and create an object to see things working.
"""

from item import item
from phone import phone
from keyboard import keybord

# Create a keyboard and print its name (uses the property from the base class)
item1 = keybord("Vivo", 100, 3)
print(item1.name)





# item.instantiate_from_csv()
# print(item.all)
# item1 = item("phone", 100,1)
# item2 = item('laptop', 1000, 3)
# item3 = item('cable', 10, 5)
# item4 = item('mouse', 50, 5)
# item5 = item("keyboard", 75, 5)
# print(item.__dict__)  # All the attributes for class level
# print(item1.__dict__) # All the attributes for instance level
# item1.apply_discount()
# print(item1.price)
# print(item.all)
# for instance in item.all:
#     print(instance.name)





