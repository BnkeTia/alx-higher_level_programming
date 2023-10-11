#!/usr/bin/python3

def multiply_by_2(a_dictionary):

    new_dictionary = {}

    for key, value in a_dictionary.items():
        new_dictionary[key] = value * 2
    return new_dictionary


# Example usage:
original_dict = {'a': 2, 'b': 4, 'c': 6}
result_dict = multiply_by_2(original_dict)
print(result_dict)
