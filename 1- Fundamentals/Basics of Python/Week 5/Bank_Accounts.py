class Bank_Account:
    def __init__(self,account_id,owner,total_amount=0):
        self.account_id = account_id
        self.owner = owner
        self.total_amount = total_amount
    def withdraw(self,amount):
        self.total_amount -= amount
    def deposit(self,amount):
        self.total_amount += amount
    def display(self):
        print("Account ID :",self.account_id)
        print("Owner :",self.owner)
        print("Total amount :",self.total_amount)