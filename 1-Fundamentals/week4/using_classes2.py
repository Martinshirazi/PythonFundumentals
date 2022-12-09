class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    
    def change_pasword(self, password):
        self.password = password
        print("your password has been changed to", self.password)
    

user1 = User("Jane", "jane@nucamp.co", "janespassword")
print(user1.password)
user1.change_pasword("NewPassword123")
