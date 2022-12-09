
x = 0

while x != 10:
    x = x + 1

    if x < 5:
        print(x)

    elif 5 <= x <= 8:
        if x == 6:
            print(x)
            continue
        print("x is bigger than or equal to 5, and less than or equal to 8, but not 6. it is : ", x)

    else:
        print("x is bigger than 8. It is:", x)