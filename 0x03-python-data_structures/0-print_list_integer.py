#!/usr/bin/python3
from typing import List, Optional

def print_list_integer(_list: Optional[List[int]] = None) -> None:
    if _list is None:
        _list = []

    for i in _list:
        print(f'{i:d}')

# Example usage:
my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)
