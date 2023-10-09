#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for row in matrix:
        # Iterarte through each column in the current row
        for column in range(len(row)):
            print("{:d}" .format(row[column]), end=" ")

            # add a space if next column is not the last
            if column < len(row) - 1:
                print(" ", end="")

        print("")  # print a new line
