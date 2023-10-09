#!/usr/bin/python3

def multiple_returns(sentence):

    if not sentence:
        return (0, None)

    len_sen = len(sentence)
    char1 = sentence[0]  # set first character to none if sentence is empty
    return (len_sen, char1)
