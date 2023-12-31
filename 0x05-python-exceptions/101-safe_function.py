#!/usr/bin/python3
from __future__ import print_function
import sys

def safe_function(fct, *args):
    try:
        res = fct(*args)
    except Exception as e:
        print(f"Exception: {e}", file=sys.stderr)
        return None
    else:
        return res

def divide(x, y):
    return x / y

result = safe_function(divide, 10, 0)
print(result)
