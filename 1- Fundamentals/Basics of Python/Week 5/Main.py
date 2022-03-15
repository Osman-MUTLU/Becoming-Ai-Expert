from Customers import Customer 

customer_1 = Customer(1,"Osman MUTLU",9000)
customer_2 = Customer(2,"Beyza GUR",4000)

customer_1.bank_account.display()
print("-------------------------")
customer_2.bank_account.display()

customer_1.bank_account.withdraw(700)
customer_2.bank_account.withdraw(300)
customer_1.bank_account.credit_withdrawal(1000)
customer_2.bank_account.credit_withdrawal(500)
print("\n**---------------------------**\n")
customer_1.bank_account.display()
print("-------------------------")
customer_2.bank_account.display()