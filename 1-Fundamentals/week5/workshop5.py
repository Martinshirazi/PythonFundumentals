import random


def guess_random_number(tries=5, start=0, stop=10):
    random_num = random.randint(start, stop)
    while tries != 0:
        print("\nNumber of tries left:", tries)
        guess = int(input(f"Guess a number between {start} and {stop}: "))

        if guess == random_num:
            print("you guessed the correct number")

        elif guess > random_num:
            print("guess lower!")

        elif guess < random_num:
            print("Guess higher!")
            tries -= 1
    print(f"You failed to guess the number:{random_num}")

#  guess_random_number()


def guess_random_num_linear(tries=5, start=0, stop=10):
    random_num = random.randint(start, stop)

    for guess in range(tries):
        print(f"Program guessing ...{guess}")
        if guess == random_num:
            print("You guessed the correct number!")
            return
        else:
            tries -= 1
            print(f"Number of tries left: {tries}")
    print(f"You failed to guess the number:{random_num}")

# guess_random_num_linear()


def guess_random_num_binary(tries=5, start=0, stop=100):
    random_num = random.randint(start, stop)
    lower_bound = start
    upper_bound = stop
    print(f"Random number is : {random_num}")
    while tries != 0:
        pivot = (lower_bound + upper_bound) // 2
        # pivot_value = the list[pivot]

        if pivot == random_num:
            print("\nYou guessed the correct number")
            return

        elif pivot > random_num:
            upper_bound = pivot - 1
            tries -= 1
            print(f"\nNumber of tries left: {tries}")
            print(f"Now Pivot point is: {pivot}")
        else:
            lower_bound = pivot + 1
            tries -= 1
            print(f"\nNumber of tries left: {tries}")
            print(f"Now Pivot point is: {pivot}")
    print("\nYou failed to guess the number!")


guess_random_num_binary()

