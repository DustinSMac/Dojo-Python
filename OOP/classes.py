class User:
    def __init__(self, name, balance):
        self.name=name
        self.balance=balance
        # self.account=BankAccount(int_rate=0.02, balance=0)
        
    def make_deposit(self,balance):
        self.balance+=balance
        return self
    
    def make_withdrawal(self, balance):
        self.balance-=balance
        return self
    
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.balance}")
        return self
        
    def transfer_money(self,other_user,balance):
        self.make_withdrawal(balance)
        other_user.make_deposit(balance)
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