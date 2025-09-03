class BankAccount():
    bank_name = 'Total Really Bank'
    annual_interest_rate = 0.04

    def __init__(self, acc_holder, balance=0):
        self.acc_holder = acc_holder
        self.balance = balance
        self.transactions = []

    
U = BankAccount("Umesh", 25000)
V = BankAccount("Vani", 1000)

# print(U.bank_name, V.bank_name, BankAccount.bank_name)

# BankAccount.bank_name='IDFC First Bank'
# print(U.bank_name, V.bank_name)
# U.bank_name='Private Bank'

# print(U.bank_name, U.annual_interest_rate)

BankAccount.annual_interest_rate=0.05
# print(U.annual_interest_rate)

print(U.balance)