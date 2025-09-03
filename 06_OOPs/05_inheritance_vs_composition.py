class Customer:
    def __init__(self, name, email):
        self.name = name 
        self.email = email

    def __str__(self) -> str:
        return f"{self.name} ({self.email})"

#composition in action(passing 'customer')
class BankAccount:
    bank_name = "Some Bank"
    
    def __init__(self, acc_no, customer, balance=0):
        self.acc_no = acc_no
        self.customer = customer 
        self.__balance = balance
    
    def deposit(self, amount):
        self.__balance += amount
        print(f"{self.customer.name} deposited {amount}. Balance = {self.__balance}")
    def withdraw(self, amount):
        if amount > self.__balance:
            print(f"Insufficient funds: {self.__balance}")
        else:
            self.__balance -= amount
            print(f"{self.customer.name} withdrew {amount}. Balance = {self.__balance}")
    def __str__(self) -> str:
        return f"Account {self.acc_no} ({self.customer.name}), Balance: {self.__balance}"
    
#specialized account(inheritance in action)
