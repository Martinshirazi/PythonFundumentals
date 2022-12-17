def linear_search_dictionary(my_dict, target):
    for i in my_dict:
        if target == my_dict[i]:
            print("Found at key", i)
    if target not in my_dict.values():
        print("Target is not in the dictionary")


my_dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}

linear_search_dictionary(my_dictionary, 5)
linear_search_dictionary(my_dictionary, 3)
linear_search_dictionary(my_dictionary, 8)
