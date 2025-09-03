class BankAccount():
    def __init__(self, acc_holder, balance=0):
        self.acc_holder = acc_holder
        self.balance = balance
        self.transactions = []

    def withdraw(self, withdrawal_amount):
        if withdrawal_amount > self.balance:
            print(f"Insufficient Balance.\n Your balance is: {self.balance}")
        else:
            self.balance -= withdrawal_amount
            self.transactions.append(-withdrawal_amount)
            print(f"Withdrew: {withdrawal_amount}.\n New Balance: {self.balance}")

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        self.transactions.append(+deposit_amount)
        print(f"Deposited {deposit_amount}.\n New balance: {self.balance}")


Umesh = BankAccount('Umesh', 25000)

print(Umesh.withdraw(2000))
print(Umesh.deposit(500))