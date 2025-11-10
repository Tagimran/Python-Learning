class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient funds!")
    
    def check_balance(self):
        print(f"{self.name}'s Balance: ₹{self.balance}")

# Example Usage
user1 = BankAccount("Imran", 1000)
user1.deposit(500)
user1.withdraw(200)
user1.check_balance()

