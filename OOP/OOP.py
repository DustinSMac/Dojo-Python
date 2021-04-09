from classes import *


#First part for User assignment
Liam = User("Liam",100)
Neil = User("Neil",100)
Harris = User("Harris",100)

Liam.make_deposit(30).make_deposit(20).make_deposit(10).display_user_balance()

Neil.make_deposit(50).make_deposit(60).make_withdrawal(100).make_withdrawal(24).display_user_balance()

Harris.make_deposit(540).make_withdrawal(26).make_withdrawal(87).make_withdrawal(32).display_user_balance()

Liam.transfer_money(Harris,30).display_user_balance()
Harris.display_user_balance()


#2nd part for BankAccount assignment
AccountA=BankAccount()
AccountA.deposit(50).deposit(50).deposit(60).withdraw(32).yield_interest().display_account_info()
AccountB=BankAccount()
AccountB.deposit(24).deposit(542).withdraw(12).withdraw(32).withdraw(53).withdraw(40).yield_interest().display_account_info()
