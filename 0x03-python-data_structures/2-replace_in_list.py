#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    try:
        my_list[idx] = element
    except IndexError:
        pass
    return my_list
