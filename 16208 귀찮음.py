# -*- coding: utf-8 -*-

n = int(input())
x = list(map(int,input().split()))

cost = 0
sum = 0
l = len(x)

for i in x:
    sum = sum + i
for i in range(0,l-1):
    sum = sum - x[i]
    cost = cost + x[i]*sum

print(cost)