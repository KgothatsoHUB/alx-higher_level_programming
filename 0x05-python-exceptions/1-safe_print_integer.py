#!/usr/bin/python3

def safe_print_integer(value):
    """
    Print an int with "{:d}".format().

    Args:
        value: The value to print.

    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(int(value)))
        return True
    except (TypeError, ValueError):
        return False

# Example usage:
result = safe_print_integer("123")
print(result)  # Output: True

result = safe_print_integer("abc")
print(result)  # Output: False
