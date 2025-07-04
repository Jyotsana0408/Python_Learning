class BankAccount:

    def __init__(self,account_holder, balance = 0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount >= 0:
            self.balance  += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Insufficient funds")

    def showBalance(self):
        print(f"Account Holder: {self.account_holder}, Balance: ₹{self.balance}")


acc = BankAccount("Jyotsna",5000)
acc.showBalance()
acc.deposit(1500)
acc.withdraw(2000)
acc.withdraw(6000) 

