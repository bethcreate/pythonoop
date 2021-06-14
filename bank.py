from datetime import datetime
class BankAccount:
    savings=3000
    fixedAccount="fixed"
    def __init__(self,name,Phone_number):
        self.name=name
        self.phone_number=Phone_number
        self.balance=0
        self.statement= []
        self.loan=0
    def show_balance(self):
        return f"hello{self.name} your balance is {self.balance}"
    def deposit(self, amount):
        try:
            10 + amount
        except TypeError:
            return f"The amount must be in figures"
        if amount <=0: 
            return f"you cannot deposit {amount}"
        else:
            
            self.balance += amount
            now=datetime.now()
            transaction={"amount":amount, "time": now, "Naration": "You deposited"}
            self.statement.append(transaction)
        return self.show_balance()

    def withdraw(self,amount):
        try:
            10 + amount
        except TypeError:
            return f"The amount must be in figures"

        if amount>self.balance:
            return f"your balance is {self.balance} you cannot withdraw"
        else:
            self.balance -= amount
            now=datetime.now()
            withdrawal={"amount":amount, "time": now, "Naration": "You withdrew"}
            self.statement.append(withdrawal)

        return self.show_balance()


   
        
    def borrow_loan(self,amount):
        try:
            10 + amount
        except TypeError:
            return f"The amount must be in figures"
        return f"Congratulation you have borrowed{amount}"
    
    def repay_loan(self,amount):
        try:
            10 + amount
        except TypeError:
            return f"the anount must be in figures"
        return f"You have successfully repaid {amount}"

    def show_statement(self):
        for transaction in self.statement:
            amount = transaction["amount"]
            Naration = transaction["Naration"]
            time = transaction["time"]
            date = time.strftime("%d/%m/%y")
            print(f"{date} {Naration} {amount}")
        return self.statement

    def borrow(self,amount):

        if amount<0:
            return f"You cannot borrow more than limit"

        elif self.loan>=0:
            return f"You can borrow"

        elif amount<0.1*self.balance:
            return f"You have reached to your loan limit"
        
        else:

            loan=amount*1.05
            self.loan=loan
            self.balance +=amount
            now=datetime.now()
            Borrow_transaction={"amount":amount, "time": now, "Naration": "You borrowed"}
            self.statement.append(Borrow_transaction)

            return f"You have to repay the existing loan" 


    def repay(self,amount):
        if amount<0:
            return f"Your balance is too low! "
        
        elif amount <= self.loan:
            return f"decrease loan with {amount}"

        elif amount< self.loan:
            self.loan-=amount
            return "You have reduced your loan"

        else:
            diff=amount-self.loan
            self.loan=0
            self.deposit(diff)
            now=datetime.now()
            repay_transaction={"amount":amount, "time": now, "Naration": "You have repayed"}
            self.statement.append(repay_transaction)

            return f"Your loan is fully repaid"

    def transfer(self,account,amount):
        try:
            10+amount
        except TypeError:
            return f"The amount should be in figures"
        fee= amount*0.05
        total=amount + fee

        if amount<0:
            return f"You are not qualified to make a transfer"
        elif total>self.balance:
            return f"your balance is {self.balance} and you need atleast {total} for this transfer "
        else:
            account.deposit(200000)
            self.balance=total
            return f"The amount has been transferred to the account number"

class Mobile_money(BankAccount):

    def __init__(self,name,Phone_number,service_provder):
        BankAccount.__ini__(name,Phone_number)
        self.service_provider=service_provder

    def buy_airtime(self,amount):
        try:
            10+amount
        except TypeError:
            return f"The anmount sghould be in figures"
        if amount<0:
            return f"You have insufficient funds" 
        elif self.balance>amount:
            return f"Your balance is low to buy this amount of credit"
        else:
            self.balance-=amount
            return f"You have purchased airtime worth {amount} from {self.service_provider}. Your account balance is {self.balance}"        












       

         











        





    

        


    