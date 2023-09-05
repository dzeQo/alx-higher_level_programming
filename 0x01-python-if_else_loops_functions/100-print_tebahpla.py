#!/usr/bin/python3
a = 122
while a >= 97:
    char1 = chr(a)
    a -= 1
    char = chr(a - 32)
    print('{}{}'.format(char1, char), end="")
    a -= 1
