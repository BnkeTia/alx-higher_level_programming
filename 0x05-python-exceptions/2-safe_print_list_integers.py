#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed_integers = 0  # set number of inegers printed to 0

        try:
            for element in my_list:
                if isinstance(element, int):
                        print("{:d}" .format(element), end="")
                        printed_integers += 1
                        if printed_integers >= x:
                            break

        except IndexError:
            pass
    print()  # Add a new line
    return printed_integers
