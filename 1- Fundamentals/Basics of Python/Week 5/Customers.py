from Credit_Accounts import Credit_Account as credit_account

class Customer:
    def __init__(self,account_id,name,total_amount=0):
        self.account_id = account_id
        self.name = name
        self.total_amount = total_amount
        self.bank_account = credit_account(account_id,name,1000,total_amount)
    