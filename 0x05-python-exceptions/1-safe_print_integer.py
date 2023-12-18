#!/usr/bin/python3

def safe_print_integer(value):
    """
    Print an integer with "{:d}".format().

    Args:
        value: The value to print.

    Returns:
        True if value has been correctly printed (it means the value is an integer),
        False otherwise.
    """
    try:
        print("{:d}".format(int(value)))
        return True
    except (ValueError, TypeError):
        return False

# Example usage:
result = safe_print_integer("123")
print(result)  # Output: True

result = safe_print_integer("abc")
print(result)  # Output: False
