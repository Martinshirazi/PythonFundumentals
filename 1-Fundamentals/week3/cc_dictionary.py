inches_snow = {"Monday": 2, "Tuesday": 4, "Wednesday": 5, "Thursday": 8, "Friday": 9, "Saturday": 6, "Sunday": 3}


def total_inches():
    print("Total snowfall inches: ", sum(inches_snow.values()))


def day_inch(userInput):
    print("How many inches of snow fell on", userInput, "?: ", inches_snow[userInput])


while True:
    user = input("What day would you like to know its snowfall measurements?\nPlease type exit to quit the program! ").capitalize()
    if user in inches_snow:
        day_inch(user)
        total_inches()
    elif user == "Quit":
        break
    else:
        print("Please enter a valid input")
        continue
