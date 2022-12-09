from banking_pkg import account


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


print("          === Automated Teller Machine ===          \n")
name = input("Enter your name to register: ")
pin = input("Enter PIN: ")
balance = 0.0
print(name.capitalize() +
      " has been registered with starting balance of $" + str(balance))
print(" ")

while True:
    print('LOGIN')
    name_to_validate = input("Enter Name: ")
    pin_to_validate = input("Enter PIN: ")

    if name == name_to_validate and pin == pin_to_validate:
        print("Login Successful")
        break
    else:
        print("Invalid Credentials!!\n\n")

while True:
    atm_menu(name)
    option = input("Choose an option: ")
    if option == '1':
        account.show_balance(balance)
    elif option == '2':
        balance = account.deposit(balance)
    elif option == '3':
        balance = account.withdraw(balance)
    elif option == '4':
        account.logout(name)
        break
    else:
        print("Wrong option!\n\n")
