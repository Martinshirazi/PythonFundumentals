def login(database, username, password):
    if username in database:
        if database[username] == password:
            print("Welcome back ", username)
            return username
        else:
            print("Invalid Password")
            return ""
    else:
        print("User not exist. Please register")
        return ""

def register(database, username, password):
    if len(username) <= 10:
        if username in database:
            print("Username already registered")
            return ""
        else:
            if len(password) < 5:
                print("Minimum 5 character required for Password")
            else:
                print(username, "has been registered")
                return username
    if len(username) > 10:
        print("Maximum 10 character is allowed for username")
        return ""
    

# mylist = {}
# name = input("user")
# password = input("password")
# mylist[name] = password
# print(mylist)