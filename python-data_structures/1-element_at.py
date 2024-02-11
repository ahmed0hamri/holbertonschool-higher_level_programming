#!/usr/bin/python3
def element_at(my_list, idx):

    return my_list[idx] if 0 < idx < len(my_list) else None


list_b = ("b", "o", "t", "o", "m", "g")
idx = 0
print("Element at index {:d} is {}".format(idx, element_at(list_b, idx)))
