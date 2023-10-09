#!/usr/bin/python3

def max_integer(my_list=[]):

    # check if the list is empty
    if not my_list:
        return None

    # Initialize a variable to store the biggest integer
    big_int = my_list[0]
    # find max integer
    for num in my_list:
        if num > big_int:
            big_int = num

    return big_int
