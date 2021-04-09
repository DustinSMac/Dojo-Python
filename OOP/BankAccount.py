class BankAccount:
    def __init__(self, rate=0.01, balance=0.00):
        self.rate = rate
        self.amount=balance
        
    def deposit(self, amount):
        self.amount+=amount
        return self
    
    def withdraw(self, amount):
        if(self.amount>amount):
            self.amount-=amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.amount-=5
        return self
    
    def display_account_info(self):
        print(f"Balance: {self.amount}")
        return self
    
    def yield_interest(self):
        if(self.amount>0):
            self.amount*=(1+self.rate)
            return self
        else:
            return False