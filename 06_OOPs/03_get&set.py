class BankAccount():
    bank_name = 'Total Really Bank'
    annual_interest_rate = 0.04

    def __init__(self, acc_holder, balance=0):
        self.acc_holder = acc_holder
        self.__balance = balance
        self.transactions = []
    
    def get_balance(self):
        return self.__balance
    
    def set_balance(self, new_balance):
        if new_balance>0:
            self.__balance = new_balance
            return self.__balance
        else:
            return("Balance Cannot be negative")

U = BankAccount("Umesh", 50000)
# print(U.balance)
# U.balance = 4500
# print(U.balance)
# print(U.__balance) #attribute error. Python hid it now.
print(U.get_balance())
print(U.set_balance(520))



print("....This was ENCAPSULTION in action....")

