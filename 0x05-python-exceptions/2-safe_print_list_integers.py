#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    Print the first x elements of a list that are int.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.

    Returns:
        The number of elements printed.
    """
    num_integers_printed = 0

    for i in range(x):
        try:
            if type(my_list[i]) == int:
                print("{:d}".format(my_list[i]), end="")
                num_integers_printed += 1
        except IndexError:
            break

    print("")
    return num_integers_printed

# Example usage:
my_list = [1, 'a', 2, 'b', 3, 'c']
num_printed = safe_print_list_integers(my_list, 4)
print(f"Number of integers printed: {num_printed}")
