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


Liam = User("Liam",100)
Neil = User("Neil",100)
Harris = User("Harris",100)

Liam.make_deposit(30).make_deposit(20).make_deposit(10).display_user_balance()

Neil.make_deposit(50).make_deposit(60).make_withdrawal(100).make_withdrawal(24).display_user_balance()

Harris.make_deposit(540).make_withdrawal(26).make_withdrawal(87).make_withdrawal(32).display_user_balance()

Liam.transfer_money(Harris,30).display_user_balance()
Harris.display_user_balance()