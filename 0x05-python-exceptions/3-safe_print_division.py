#1/usr/binpython3
def safe_print_division(a, b):
    try:
        ratio = a / b
    except ZeroDivisionError:
        ratio = None

    finally:
        print("Inside result: {}" .format(ratio))
        return ratio
