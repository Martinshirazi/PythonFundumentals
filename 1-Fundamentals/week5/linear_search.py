def linear_search(the_list, target):
    for x in range(len(the_list)):
        if the_list[x] == target:
            print("Found at index", x)
            return x
    print("Target is not in the list")
    return -1


my_list = [6, 3, 4, 2, 5, 7]
"""range(start, stop, step value) here step and start value are default to 1 and 0 respectively
range(0, len(the_list), 1)"""
linear_search(my_list, 5)
linear_search(my_list, 3)
linear_search(my_list, 8)

"""Using this method works only for list which is ordered, if we were going to use another data structure, 
that would be a totally different approach."""

"""sorted data lists are more efficient being used for BINARY SEARCH """
