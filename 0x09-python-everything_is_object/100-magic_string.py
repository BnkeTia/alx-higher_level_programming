#!/usr/bin/pythons3
def magic_string(n=1):
    return "BestSchool" + (", " + magic_string(n - 1) if n > 1 else "")
