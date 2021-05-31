from datetime import datetime
class BankAccount:
    savings=3000
    fixedAccount="fixed"
    def __init__(self,name,phone_number):
        self.name=name
        self.phone_number=phone_number
        self.balance=0
        self.statement= []
    def show_balance(self):
        return f"hello{self.name} your balance is {self.balance}"
    def deposit(self, amount):
        if amount <=0: 
            return f"you cannot deposit {amount}"
        else:
            
            self.balance += amount
            now=datetime.now()
            transaction={"amount":amount, "time": now, "Naration": "You deposited"}
            self.statement.append(transaction)
        return self.show_balance()

    def withdraw(self,amount):
        if amount>self.balance:
            return f"your balance is {self.balance} you cannot withdraw"
        else:
            self.balance -= amount
            now=datetime.now()
            withdrawal={"amount":amount, "time": now, "Naration": "You withdrew"}
            self.statement.append(withdrawal)

        return self.show_balance()


   
        
    def borrow_loan(self,amount):
        return f"Congratulation you have borrowed{amount}"
    
    def repay_loan(self,amount):
        return f"You have successfully repaid {amount}"

    def show_statement(self):
        for transaction in self.statement:
            amount = transaction["amount"]
            Naration = transaction["Naration"]
            time = transaction["time"]
            date = time.strftime("%d/%m/%y")
            print(f"{date} {Naration} {amount}")
        return self.statement

    

        


    