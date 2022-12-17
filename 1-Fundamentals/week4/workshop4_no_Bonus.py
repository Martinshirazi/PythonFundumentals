class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, name):
        self.name = name

    def change_pin(self, pin):
        self.pin = pin

    def change_password(self, password):
        self.password = password

    def __repr__(self):
        return self.name + " " + str(self.pin) + " " + self.password


class BankUser(User):
    def __init__(self, name, pin, password, balance=0):
        super().__init__(name, pin, password)
        self.balance = balance

    def __repr__(self):
        return super().__repr__() + " and Balance of: " + str(self.balance)

    def show_balance(self):
        print(self.name, "has an account balance of: $", self.balance)

    def withdraw(self, balance):
        if balance > self.balance:
            print("Insufficient amount, please try lower amount")
        else:
            self.balance = self.balance - balance

    def deposit(self, amount):
        self.balance = amount + self.balance

    def transfer_money(self, amount, to_user):
        print("You are transferring: $" + str(amount), "to", to_user.name)
        pin = input("Authentication required\nPlease enter your PIN: ")
        if self.pin == int(pin):
            print("Transfer Authorized!Proceeding...")
            print("transferring ", amount, "to ", to_user.name)
            self.balance = self.balance - amount
            to_user.balance = to_user.balance + amount
            self.show_balance()
            to_user.show_balance()
        else:
            print("Invalid PIN, validation Failed!!!")

    def request_money(self, amount, from_user):
        print("You are requesting $" + str(amount), "from:", from_user.name, "\nUser Authentication Required!")
        pin = input("Please Enter " + from_user.name + "'PIN:")
        if from_user.pin == int(pin):
            password = input('Please Enter your PassWord: ')
            if self.password == password:
                print("Transfer Authorized!Proceeding...")
                print("transferring ", amount, "from ", from_user.name, "To", self.name)
                from_user.balance = from_user.balance - amount
                self.balance = self.balance + amount
                self.show_balance()
                from_user.show_balance()
            else:
                print('Password Validation failed')
        else:
            print("PIN is invalid")


user_1 = BankUser("Martin", 123, "MyPassMartin", 500)
user_2 = BankUser("Timo", 456, "MyPassTimo", 100)
user_3 = BankUser("Lucy", 789, "MyPassLucy", 200)
"""Driver Code for Task 1"""
# user_1 = User("Bob", 1234, "Password")
# print(user_1.name, user_1.pin, user_1.password)

"""Driver Code for Task 2"""
# user_1 = User("Bob", 1234, "Password")
#
# user_1.change_name("Martin")
# user_1.change_pin(4567)
# user_1.change_password("MyNewPassword")
# print(user_1)

"""Drive Code for Task 3"""
# user_1 = BankUser("MARTIN", 1234, "MyBankPassword", 500)
# print(user_1)

"""Driver Code for Task 4"""
# user_1 = BankUser("Martin", 123, "MyBankPassword", 500)
# user_2 = BankUser("Timo", 456, "MyPassTimo", 100)
# user_3 = BankUser("Lucy", 789, "MyPassLucy", 200)
# # user_1.show_balance()
# user_1.deposit(100)
# user_1.show_balance()
# user_1.withdraw(610)
# user_1.show_balance()
# print(user_1)

"""Driver Code for Task 5"""
# user_1.transfer_money(50, user_2)
# user_1.show_balance()
# user_2.show_balance()
# print(user_2)
# print(user_1)
#
# user_1.request_money(100, user_3)
# print(user_3)
# print(user_1)
