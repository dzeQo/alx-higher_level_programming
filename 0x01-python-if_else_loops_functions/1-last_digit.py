#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
i = abs(number) % 10
if number < 0:
    i *= -1
print("Last digit of", number, "is", i, end=" ")
if i > 5:
    print("and is greater than 5")
elif i == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
