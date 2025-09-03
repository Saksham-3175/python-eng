class BankAccount():
    bank_name = 'Some Bank'
    annual_interset_rate = 0.04

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
            return("Balance cannot be negative!")
    
    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.__balance:
            print(f"Insufficient Balance.\n Your balance is: {self.__balance}")
        else:
            self.__balance -= withdraw_amount
            self.transactions.append(-withdraw_amount)
            print(f"Withdrew: {withdraw_amount}.\n New Balance: {self.__balance}")
    
    def deposit(self, deposit_amount):
        self.__balance += deposit_amount
        self.transactions.append(+deposit_amount)
        print(f"Deposited {deposit_amount}.\n New Balance: {self.__balance}")

class SavingsAccount(BankAccount):
    def __init__(self, acc_holder, balance=0, interest_rate=0.04):
        super().__init__(acc_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.__balance * self.interest_rate
        self.deposit(interest)
        print(f"Interest Added: {interest}")
    
    def limit_withdrawl(self):
        pass

    def service_fee(self, withdraw_amount):
        withdraw_amount += 50
        self.withdraw(withdraw_amount)


class CurrentAccount(BankAccount):
    def __init__(self, acc_holder, balance=0):
        super().__init__(acc_holder, balance)

    def withdraw(self, withdraw_amount):
        total_withdraw = withdraw_amount + 50
        print("A service fee of 50 credits is being applied as per the T&C.")
        super().withdraw(total_withdraw)
    ## balance can never be 0.....
    ## if urgent, add up th 50 credits for next transaction

U = BankAccount("Some User", 50000)
V = SavingsAccount("User 1", 23000, 0.07)
W = CurrentAccount("New User", 500)

W.withdraw(500)



