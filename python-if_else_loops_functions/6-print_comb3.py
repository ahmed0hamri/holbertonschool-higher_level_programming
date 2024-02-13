#!/usr/bin/python3
#!/usr/bin/python3
for j in range(10):
    for d in range(10):
        if j != d and j * 10 + d < d * 10 + j:
            if j != 8 or d != 9:
                print("{}{}, ".format(j, d), end="")
            else:
                print("{}{}".format(j, d))
