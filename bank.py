class BankAccount:
    savings=3000
    fixedAccount="fixed"
    def __init__(self,balance,accountNumber):
        self.balance=balance
        self.accountNumber=accountNumber
    def withdraw(self):
        return f" my account had{self.balance} but I withdrew some cash"
    def deposit(self):
        return f" i will deposit 1000 to {self.accountNumber}"