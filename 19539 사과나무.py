# -*- coding: utf-8 -*-

n = int(input())

heights = list(map(int,input().split()))

d = 0
r = 0

for i in heights:
    d += i // 2
    r += i % 2

if (d - r) % 3 == 0 and d >= r:
    print("YES")
else:
    print("NO")