from Bank_Accounts import Bank_Account

class Credit_Account(Bank_Account):
    def __init__(self, account_id, owner,limit, total_amount=0):
        super().__init__(account_id, owner, total_amount)
        self.limit = limit
    def credit_withdrawal(self, amount):
        if self.limit - amount >= 0:
            self.limit -= amount
        else:
            print("You have not enough limit on credit cards.")
    def display(self):
        super().display()
        print("Limit : {}".format(self.limit))
            