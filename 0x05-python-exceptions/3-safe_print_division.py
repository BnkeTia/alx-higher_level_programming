#!/usr/bin/python3
def safe_print_division(a, b):
    ratio = None
    try:
        ratio = a / b
    except ZeroDivisionError:
        ratio = None

    finally:
        print("Inside result: {}" .format(ratio))
        return ratio
