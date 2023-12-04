#!/usr/bin/python3

from typing import List

def print_list_integer(_list: List[int] = None) -> None:
    if _list is None:
        _list = []
    
    for i in _list:
        print(f'{i:d}')
