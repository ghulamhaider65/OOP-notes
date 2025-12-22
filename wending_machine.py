# Class for products

class product:
    def __init__(self ,code, name, price, quantity):
        self.code = code
        self.name = name
        self.price = price
        self.quantity = quantity

    def is_available(self):
        return self.quantity > 0
    
    def dispance(self):
        if self.is_available():
            self.quantity -=1
            return True
        return False
    
# Class for wending machine

class VendingMachine:
    def __init__(self):
        self.products = {}
        self.balance = 0

    def add_product(self, product):
        self.products[product.code] = product

    def display_products(self):
        print("\nAvailable items")

        for p in self.products.values():
            print(f"code: {p.code} | {p.name} | price: {p.price} | Stock : {p.quantity}")

    def insert_money(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            print(f"Inserted: {amount}")
            print(f"Current balance: {self.balance}")

        else:
            print("Invalid ammount")

    def select_product(self, code):
        if code not in self.products:
            print("Invalid product code")
            return
        
        product = self.products[code]
        if not product.is_available():
            print("product is out of stock")

        if self.balance < product.price:
            print("Insufficient balance")
            return
        
        # Dispance product

        product.dispance()
        self.balance = self.balance - product.price
        print(f"Dispensed: {product.name}")
        self.return_change()

    def return_change(self):
        if self.balance > 0:
            print(f"Returning change : {self.balance}")
            self.balance = 0


def main():
    vm = VendingMachine()
    vm.add_product(product("A1", "Chips", 50, 5))
    vm.add_product(product("A2", "Soda", 80, 3))
    vm.add_product(product("B1", "Chocolate", 100, 2))

    while True:
        vm.display_products()

        print("\n1. Insert Money")
        print("2, select product")
        print("3, Exit")

        choice = input("choose an option:")

        if choice == "1":
            amount = int(input("Enter ammount: "))
            vm.insert_money(amount)

        elif choice == "2":
            code = input("Enter product code: ").upper()
            vm.select_product(code)

        elif choice == "3":
            print("Thank you for using the vanding machine")
            break

        else:
            print("Invalid option")

main()