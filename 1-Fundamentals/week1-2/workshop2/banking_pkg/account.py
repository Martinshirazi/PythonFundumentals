def show_balance(balance):
    print("The current balance is: $"+str(balance))


def deposit(balance):
    amount = input("Enter the amount to deposit: ")
    return balance + float(amount)


def withdraw(balance):
    while True:
        amount = input("Enter amount to withdraw: ")
        if float(amount) <= balance:
            return balance - float(amount)
        else:
            print("Insufficient fund! \n Please try lower amount.")


def logout(name):
    print("\nGoodbye", name+"!!!\n")
