#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    printed_elements = min(x, len(my_list)) 
    for item in my_list[:x]:  
        print(item, end=" ")
    print() 
    return printed_elements


my_list = [1, 2, 3, 4, 5]
num_printed = safe_print_list(my_list, 3)
print("Number of elements printed:", num_printed)
