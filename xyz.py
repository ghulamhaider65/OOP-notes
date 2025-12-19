class Atm:
    # constructor
    def __init__(self):
        self.balance = 1000
        self.pin = ""

    # Menu method
    def menu(self):
        while True:
            user_input = input("""
                     Hello! Welcome to the ATM
                        Please choose an option:
                        1. Create Pin
                        2. Deposit
                        3. Withdraw
                        4. Check Balance
                        5. Exit
                           
""")    
            if user_input == "1":
                self.create_pin()

            elif user_input == "2":
                self.deposit()
            elif user_input == "3":
                self.withdraw()
            elif user_input == "4":
                self.check_balance()
            else:
                self.exit()
                break

    # Create pin method
    def create_pin(self):
        self.pin = input("Please enter a new PIN: ")
        print("Pin created")
    # Deposit method
    def deposit(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            amount = int(input("Enter amount to deposit: "))
            self.balance = self.balance + amount
            print("Deposit successful")
        else:
            print("Invalid Pin")
        
    # Withdraw method
    def withdraw(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            amount = int(input("Enter the amount"))
            if amount <= self.balance:
                self.balance = self.balance - amount
                print("Withdraw successful")
            else:
                print("Insufficient balance")
        else:
            print("Invalid Pin")

    # Balance check method
    def check_balance(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            print(f"your balance is {self.balance}")
        else:
            print("Invalid Pin")
    # Exit method        
    def exit(self):
        print("Thank you for using the ATM. Goodbye!")

atm = Atm()
atm.menu()