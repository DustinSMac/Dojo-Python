class User:
    def __init__(self, name, amount=100):
        self.name=name
        self.amount=amount
        
    def make_deposit(self,amount):
        self.amount+=amount
        return self
    
    def make_withdrawal(self, amount):
        self.amount-=amount
        return self
    
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")
        return self
        
    def transfer_money(self,other_user,amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self
