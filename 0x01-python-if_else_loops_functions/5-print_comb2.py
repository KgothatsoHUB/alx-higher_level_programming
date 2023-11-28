#!/usr/bin/python3
formatted_numbers = ', '.join("{:02d}".format(i) for i in range(100))
print(formatted_numbers)
