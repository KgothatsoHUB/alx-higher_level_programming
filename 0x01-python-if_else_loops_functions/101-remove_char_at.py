#!/usr/bin/python3
def remove_char_at(s, index):
    if index < 0:
        return s
    return s[:index] + s[index + 1:]

# Example usage:
# result = remove_char_at("example", 2)
# print(result)
