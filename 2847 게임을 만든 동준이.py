# -*- coding: utf-8 -*-

n = int(input())
y = []

for i in range(n):
    y.append(int(input()))#뒤에 하나하나 채워 넣는다

y.reverse()#배열을 뒤집어 준다
max = y[0]
count = 0

for i in range(1 , n):
    while max <= y[i]:
        y[i] -= 1
        count += 1
    max = y[i]


print(count)
