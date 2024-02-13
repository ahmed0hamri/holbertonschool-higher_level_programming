#!/usr/bin/python3
for z in range(10):
    for b in range(10):
        if z != b:
            print("{}{}, ".format(z, b), end="")
else:
    print("{}{}".format(z, b))
