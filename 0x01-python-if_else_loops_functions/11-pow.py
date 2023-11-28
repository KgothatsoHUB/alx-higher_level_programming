#!/usr/bin/python3

def power(base, exponent):
    # Input validation
    if not isinstance(base, (int, float)) or not isinstance(exponent, int):
        raise ValueError("Base must be a number, and exponent must be an integer.")

    # Handle special case: 0^0 is undefined
    if base == 0 and exponent == 0:
        raise ValueError("0^0 is undefined.")

    # Handle negative exponent by taking the reciprocal of the result
    result = base ** exponent if exponent >= 0 else 1 / (base ** abs(exponent))
    return result

# Example usage:
a = 2
b = 3
result = power(a, b)
print(f"{a} ^ {b} = {result}")

