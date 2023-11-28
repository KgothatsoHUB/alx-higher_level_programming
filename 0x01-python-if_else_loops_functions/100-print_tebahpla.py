#!/usr/bin/python3

# Print reversed uppercase alphabet
for ascii_value in range(122, 96, -1):
    if ascii_value % 2 != 0:
        uppercase_value = ascii_value - 32
    else:
        uppercase_value = ascii_value

    print("{:c}".format(uppercase_value), end="")
