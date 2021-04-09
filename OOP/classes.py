class User:
    def __init__(self, name):
        self.name=name
        self.account=BankAccount(rate=0.02, balance=0)
        
    def make_deposit(self,amount):
        self.account.balance+=amount
        return self
    
    def make_withdrawal(self, amount):
        self.account.balance-=amount
        return self
    
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account.balance}")
        return self
        
    def transfer_money(self,other_user,amount):
        self.account.withdraw(amount)
        other_user.account.deposit(amount)
        return self

class BankAccount:
    def __init__(self, rate=0.01, balance=0.00):
        self.rate = rate
        self.balance=balance
        
    def deposit(self, balance):
        self.balance+=balance
        return self
    
    def withdraw(self, balance):
        if(self.balance>balance):
            self.balance-=balance
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance-=5
        return self
    
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
    
    def yield_interest(self):
        if(self.balance>0):
            self.balance*=(1+self.rate)
            return self
        else:
            return False