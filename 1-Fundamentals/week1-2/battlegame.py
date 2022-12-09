wizard = "wizard"
wizard_hp = 70
wizard_damage = 150

elf = "elf"
elf_hp = 100
elf_damage = 100

human = "human"
human_hp = 150
human_damage = 20

orc = "orc"
orc_hp = 250
orc_damage = 30

dragon_damage = 50
dragon_hp = 300

exit = False

while not exit:

    # Leave the Variable and constants out of loop, so you don't run them every loop.!
    # In this loop we select our character and print the hp and damage for the user:
    while True:
        Character = input("1)Wizard\n2)Elf\n3)Human\n4)Orc\n5)Exit\nPlease choose your character:")

        if Character == "1" or Character.lower() == wizard.lower():
            Character = wizard
            my_hp = wizard_hp
            my_damage = wizard_damage
            break

        elif Character == "2" or Character.lower() == elf.lower():
            Character = elf
            my_hp = elf_hp
            my_damage = elf_damage
            break

        elif Character == "3" or Character.lower() == human.lower():
            Character = human
            my_hp = human_hp
            my_damage = human_damage
            break

        elif Character == "4" or Character.lower() == orc.lower():
            Character = orc
            my_hp = orc_hp
            my_damage = orc_damage
            break

        elif Character == "5" or Character.lower() == "exit":
            exit = True
            print("Game has been terminated")
            break
        else:
            print("Unknown Character")
            print("")

    if exit:
        break

    # instead of having these lines at the end of each if statement, we can leave them at the end and write once.
    print("you have selected character: ", Character)
    print("Your HP is: ", my_hp)
    print("Your Damage is: ", my_damage)
    print("")

    # In this While loop we run the battle. hp and hits in the results are shown from this part of the code.
    while True:
        dragon_hp = dragon_hp - my_damage
        print("The ", Character, "damaged the dragon!\nThe Dragon's hitpoints are now: ", dragon_hp)
        print("")

        if dragon_hp <= 0:
            print("The Dragon has lost the battle")
            break

        my_hp = my_hp - dragon_damage
        print("The Dragon damaged ", Character, "\nThe ", Character, "'s hitpoints are now: ", my_hp)

        if my_hp <= 0:
            print(Character, " has lost the battle")
            break

    play_again = input("Would like to play again?(Y/N): ")
    if play_again == 'y' or play_again == 'Y':
        continue
    else:
        exit = True
