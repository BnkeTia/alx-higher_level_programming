#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    try:
        integer = int(value)
        print("{:d}" .format(integer))
        return True
    except (ValueError, TypeError):
        sys.stderr.write("Exception: {}\n" .format(value))
        return False
