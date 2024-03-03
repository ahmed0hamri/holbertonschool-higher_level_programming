def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except:
        return False

# Example usage:
print(safe_print_integer(10))  # True
print(safe_print_integer("Hello"))  # False
