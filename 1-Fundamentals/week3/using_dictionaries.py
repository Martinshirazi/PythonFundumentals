states_capitals = {"Washington":"Seattle", "Oregon": "Salem", "California": "Sacramento"}
print(states_capitals)

states_capitals["Washington"] = "Aberdeen"
print(states_capitals)
states_capitals["Texas"] = "Austin"
print(states_capitals)

del states_capitals["California"] #NO RETURN VALUE
print(states_capitals)

# states_capitals.pop("Oregon") #IT CAN RETURN A VALUE LIKE THE LINE BELOW
removed_pair = states_capitals.pop("Oregon")
print(states_capitals)
print(removed_pair)