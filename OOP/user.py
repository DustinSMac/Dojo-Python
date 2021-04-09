class User:
    def __init__(self, name, amount=100):
        self.name=name
        self.amount=amount
        
    def make_deposit(self,amount):
        self.amount+=amount
    
    def make_withdrawal(self, amount):
        self.amount-=amount
    
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")
        
    def transfer_money(self,other_user,amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)


Liam = User("Liam",100)
Neil = User("Neil",100)
Harris = User("Harris",100)

Liam.make_deposit(30)
Liam.make_deposit(20)
Liam.make_deposit(10)
Liam.make_withdrawal(40)
Liam.display_user_balance()

Neil.make_deposit(50)
Neil.make_deposit(60)
Neil.make_withdrawal(100)
Neil.make_withdrawal(24)
Neil.display_user_balance()

Harris.make_deposit(540)
Harris.make_withdrawal(26)
Harris.make_withdrawal(87)
Harris.make_withdrawal(32)
Harris.display_user_balance()

Liam.transfer_money(Harris,30)
Liam.display_user_balance()
Harris.display_user_balance()