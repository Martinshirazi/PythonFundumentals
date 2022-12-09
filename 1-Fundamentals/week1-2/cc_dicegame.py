import random

high_score = 0


def dice_game():
    global high_score
    while True:
        user_input = int(input("Please choose a number: \n"))

        if user_input == 1:
            dice1 = random.randint(1, 6)
            print("You roll a ..", dice1,"\n")
            dice2 = random.randint(1, 6)
            print("You roll a ..", dice2,"\n")
            total = dice1 + dice2
            print("you have rolled a total of :", total,"\n")
            if total >= high_score:
                high_score = total
                print("Your highest score is:", high_score,"\n")
            else:
                print("Your highest score is:", high_score,"\n")

        elif user_input == 2:
            print("You left the game")
            break

        else:
            print("you entered an invalid argument, please try again\n")
            continue


print("Current High score: ", high_score)
print("1) Roll Dice")
print("2) Leave the Game")
dice_game()
