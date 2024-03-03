#!/usr/bin/python3


def THE_function(THE_list=[], THE_number=0):
    THE_count = 0
    try:
        for i in range(THE_number):
            print(THE_list[i], end=" ")
            THE_count += 1
    except IndexError:
        pass  # If the index is out of range, just continue without printing
    finally:
        print()  # Print a new line after printing the elements
    return THE_count
