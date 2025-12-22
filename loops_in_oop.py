class Class:
    def __init__(self):
        self.students = []

    def add_student(self, name):
        self.students.append(name)

    def show_students(self):
        for s in self.students:
            print(s)

# # testing
# room = Class()
# room.add_student("haider")
# room.add_student("sara")
# room.add_student("malik")
# room.add_student("Ali")
# room.show_students()

# while loop with object shate

class Counter:
    def __init__(self, limit):
        self.count = 0
        self.limit = limit

    def start(self):
        while self.count < self.limit:
            print("count", self.count)
            self.count = self.count + 1
# testing

# c = Counter(100)
# c.start()

# for loop for multiple objects

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Store:
    def __init__(self):
        self.products = []

    def add_products(self, product):
        self.products.append(product)

    def show_products(self):
        for p in self.products:
            print(p.name, " ", p.price)

# testing

s = Store()
s.add_products(Product("Pen", 10))
s.add_products(Product("Bood", 200))
s.add_products(Product("Bag", 1500))

s.show_products()