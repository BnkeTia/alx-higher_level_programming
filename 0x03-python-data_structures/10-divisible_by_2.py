#!/usr/bin/python3

def divisible_by_2(my_list=[]):

    # Initialize a new_list to keep True/False values
    new_list = []

    # Iterate through the original list
    for integer in my_list:

        # Check if the integer is an even number
        is_even = integer % 2 == 0
        new_list.append(is_even)

    return new_list
