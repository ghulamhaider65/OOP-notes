class BankAccount:
    def __init__(self, account_number, balance = 0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print(f"withdraw successfull and your current balance is {self.balance}")
        else:
            print("insuffiecient balance")
        
class Customer:
    def __init__(self, name, account):
        self.name = name
        self.account = account

    def display_details(self):
        print(f"Name: {self.name}, account_number {self.account.account_number}, balance: {self.account.balance}, ")

account = BankAccount("1234", 1900)
customer = Customer("Haider", account)

customer.display_details()
customer.account.deposit(500)
customer.account.withdraw(200)
# **************************************************************************************************************
