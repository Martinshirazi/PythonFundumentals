import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []


def run_the_game():
    card = random.choice(diamonds)
    hand.append(card)
    diamonds.remove(card)
    print("Your Hand: ", hand)
    print("Remaining cards: ", diamonds)


while diamonds:
    option = input("Press Enter to pick a card, or Q then enter to quit: ").capitalize()
    if option == "":
        run_the_game()

    elif option == "Q":
        break
    else:
        print("Please enter a valid input")
        continue
else:
    print("There is no more cards to pick")

# run_the_game()