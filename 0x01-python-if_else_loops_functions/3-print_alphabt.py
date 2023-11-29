#!/usr/bin/python3
for character in range(ord('a'), ord('z') + 1):
    if character not in [ord('e'), ord('q')]:
        print(chr(character), end='')
