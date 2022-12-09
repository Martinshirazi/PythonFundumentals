from donations_pkg.homepage import show_homepage, donate,show_donations
from donations_pkg.user import login, register
database = {"admin": "pas"} 
donations = []
authorized_user = ""


while True:
    show_homepage()

    if authorized_user == "":
        print("You must be logged in to donate")
    else:
        print("Logged in as:", authorized_user)

    user_input = input("Choose an option: ")
    if user_input == "1":
        username = input("Enter username: ").lower()    
        password = input("Enter password: ")
        authorized_user = login(database, username, password)
   
    elif user_input == "2":
        username = input("Enter username: ").lower()
        password = input("Enter password: ")
        authorized_user = register(database, username, password)
        if authorized_user != "":
            database[authorized_user] = password
    
    elif user_input == "3":
        if authorized_user == "":
            print("You are not logged in\n")
        else:
            donation_string = donate(authorized_user)
            donations.append(donation_string)
          

    elif user_input == "4":
        if authorized_user == "":
            print("You are not logged in!")
        else:
            show_donations(donations, authorized_user)
            print("Total donated amount: ",sum(donations))
    elif user_input == "5":
        print("\nLeaving donateMe...")
        break

