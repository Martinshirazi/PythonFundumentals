states_capitals = {"Washington":"Seattle", "Oregon": "Salem", "California": "Sacramento"}


for state in states_capitals:
    print(state) #it only prints keys

for city in states_capitals.values():
    print(city)


for state in states_capitals:
    print(states_capitals[state], "is the capital of", state)

for state, city in states_capitals.items():
    print(city, "is the capital of", state)

def donate(username):
    donation_amt = float(input("Enter amount to donate: "))
    donation_string = (username + " donated $"+ str(donation_amt))
    print(donation_string)

donate("Martin")