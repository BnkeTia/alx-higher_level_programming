#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed_integers = 0  # set number of inegers printed to 0
    for element in my_list:
        try:
            print("{:d}" .format(element), end="")
            printed_integers += 1
            if printed_integers >= x:
                break

        except (ValueError, TypeError):
            pass
    print()  # Add a new line
    return printed_integers
