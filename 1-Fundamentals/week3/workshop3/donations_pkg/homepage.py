def show_homepage():

    print("         ===DonateMe Homepage===     ")
    print('----------------------------------------------')
    print('| 1.    Login      | 2.    Register          |')
    print('----------------------------------------------')
    print('| 3.    Donate     | 4.    Show Donations    |')
    print('----------------------------------------------')
    print('|                5. Exit                     |')
    print('----------------------------------------------')


def donate(username):
    while True:
        user_input = input("Enter amount to donate: ")
        if user_input.isdigit:
            donation_amt = int(user_input)
            if donation_amt > 0:
                print(username, " donated $", donation_amt)
                print("Thank you for your donation! ")
                return donation_amt
            else:
                print("Please enter a positive number")
        else:
            print("Please enter a valid input!")



def show_donations(donations, username):
    print("\n---All Donations---")
    if len(donations) == 0:
        print("Currently, there are no donations")
    else:
        for i in donations:
            print(username," donated ", i)


# mylist = {}
# name = input("user")
# password = input("password")
# mylist[name] = password
# print(mylist)