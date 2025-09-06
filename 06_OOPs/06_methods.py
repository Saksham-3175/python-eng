#@property method

raw_dict = {"holder": "holder_name", "balance":2500}

class BankAccount:
    def __init__(self, holder, balance=0.0):
        self.holder = holder
        self.__balance = float(balance)

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative!!!")
        self.__balance = float(value)

    

acc = BankAccount("name", 1000)
acc.balance += 250



#@classmethod


