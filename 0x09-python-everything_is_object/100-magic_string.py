#!/usr/bin/python3
def magic_string(n=1, s=""):
    return "BestSchool" + s if n == 1 else magic_string(n -1, "BestSchool" + s)
