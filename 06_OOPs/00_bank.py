balance_amount = 545
acc_holder = "Name"
transactions = [0,0]


bank = {
    'balance': 545,
    'acc_holder':acc_holder,
    'transactions':transactions
}

def withdraw_money(bank):
    print(f"Balance amount: {bank.get('balance')}")
    withdrawl_amt = int(input("Enter amount to withdraw: "))
    new_amount = (bank.get('balance') - withdrawl_amt)
    print(f"You have withdrawn: {withdrawl_amt}")
    print(f"New balance: {new_amount}")
    return new_amount

withdraw_money(bank)