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
    
#specialized accounts(inheritance in action)
class SavingsAccount(BankAccount):
    def __init__(self, acc_no, customer, balance=0, interest_rate=0.04):
        super().__init__(acc_no, customer, balance)
        self.interest_rate = interest_rate
    
    def add_interest(self):
        interest = (self.interest_rate * self.__balance)
        self.deposit(interest)
        print(f"{self.customer.name}: Interest {interest} added!")

class CurrentAccount(BankAccount):
    
    def __init__(self, acc_no, customer, balance=0, fee=73):
        super().__init__(acc_no, customer, balance)
        self.fee = fee

    def withdraw(self, amount):
        total = (amount + self.fee)

        if total > self.__balance:
            print(f"{self.customer.name}: Insufficient Funds (need{total})")
        else:
            self.__balance -= total
            print(f"{self.customer.name}: Withdrew {amount} + fee({self.fee}). Balance = {self.__balance}")
    
    def __str__(self) -> str:
        return f"Account {self.acc_no} ({self.customer.name}), Balance: {self.__balance}"


        


#customers
cust_1 = Customer("cust_1", "cust1@mail.com")
cust_2 = Customer("cust_2", "cust2@mail.com")

#accounts
acc1 = SavingsAccount("S001", cust_1, 20000)
acc2 = CurrentAccount("C001", cust_2, 1500)

#actions
acc1.deposit(200)
acc1.withdraw(500)
# acc1.add_interest()

acc2.deposit(1500)
acc2.withdraw(3700)
acc2.withdraw(150)

print(acc1)
print(acc2)