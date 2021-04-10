# -*- coding: utf-8 -*-

a = input()
b = 1000 - int(a)
count = 0

while b != 0:
    if b >= 500:
        b -= 500
        count += 1
        continue
    elif b >= 100:
        b -= 100
        count += 1
        continue
    elif b >= 50:
        b -= 50
        count += 1
        continue
    elif b >= 10:
        b -= 10
        count += 1
        continue
    elif b >= 5:
        b -= 5
        count += 1
        continue
    elif b >= 1:
        b -= 1
        count += 1
        continue

print(count)