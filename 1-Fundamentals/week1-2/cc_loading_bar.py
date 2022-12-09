for amount_loaded in range(0, 101, 5):
    if amount_loaded == 25:
        print(amount_loaded)
        print("you are 1/4 of the way there")
    elif amount_loaded == 50:
        print(amount_loaded)
        print('you are half way there')
    elif amount_loaded == 75:
        print(amount_loaded)
        print('you are 3/4 of the way there')
    elif amount_loaded == 100:
        print(amount_loaded)
        print("load complete!")
    else:
        print(amount_loaded)