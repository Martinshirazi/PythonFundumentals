def binary_search(the_list, target):
    lower_bound = 0
    upper_bound = len(the_list) - 1

    while lower_bound <= upper_bound:
        pivot = (lower_bound + upper_bound) // 2
        """Floor division is necessary here to get a round number instead of 2.5 for example"""
        pivot_value = the_list[pivot]
        if pivot_value == target:
            return pivot
        if pivot_value > target:
            upper_bound = pivot - 1  # because pivot point was in half. so we have to pick the previous value as
            # upper_bound
        else:
            lower_bound = pivot + 1
    return -1  # -1 here means no index have found that matches our target


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(my_list, 10))
print(binary_search(my_list, 4))
print(binary_search(my_list, 33))
