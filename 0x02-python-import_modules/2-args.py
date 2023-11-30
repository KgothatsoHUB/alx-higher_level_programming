#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    arg_len = len(sys.argv)

    if arg_len == 1:
        print("{} argument{}.".format(arg_len - 1, '' if arg_len == 2 else 's'))
    else:
        print("{} arguments:".format(arg_len - 1))

    for i in range(1, arg_len):
        print("{}: {}".format(i, sys.argv[i]))
