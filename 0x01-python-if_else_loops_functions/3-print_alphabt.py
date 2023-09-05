 = 97
while a <= 122:
    if a == 101 or a == 113:
        a += 1
        continue
    print("{}".format(chr(a)), end="")
    a += 1
