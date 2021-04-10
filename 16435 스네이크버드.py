# -*- coding: utf-8 -*-

n , s = (map(int, input().split()))#map 함수를 이용해 각각 객체로 만듬
fruits = list(map(int, input().split()))
fruits.sort()

for i in range(n):
    if s >= fruits[i]:
        s += 1

print(s)