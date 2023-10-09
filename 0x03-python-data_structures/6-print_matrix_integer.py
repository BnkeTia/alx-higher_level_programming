#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        # Iterarte through each integer in the current row
        for integer in range(len(row)):
            print("{:d}" .format(row[integer]), end=" ")
            # add a space if next integer is not the last
            if integer < len(row) - 1:
                print(" ", end="")

        print()  # print a new line
