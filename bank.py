class BankAccount:
    savings=3000
    fixedAccount="fixed"
    def __init__(self,name,phone_number):
        self.name=name
        self.phone_number=phone_number
        self.balance=0
    def show_balance(self):
        return f"hello{self.name} your balance is {self.balance}"
    def deposit(self, amount):
        if amount <=0:
            return f"you cannot deposit {amount}"
        else:
            
            self.balance += amount
            return self.show_balance()
    def withdraw(self,amount):
        if amount>self.balance:
            return f"your balance is {self.balance} you cannot withdraw"
        else:
            self.balance -= amount
            return f"Hello, your balance is {self.balance} you cannot withdraw {money}"
   
        
    def borrow(self,amount):
        return f"Congratulation you have borrowed{amount}"
    
    def repay(self,amount):
        return f"You have successfully repaid {amount}"
        


    