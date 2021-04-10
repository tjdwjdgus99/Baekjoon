# -*- coding: utf-8 -*-

a = int(input())
b = list(map(int, input().split()))
#공백을 기준으로 구분하여 입력 받기
num = 0

b.sort() #정렬

for i in range(a):
    for j in range(i + 1):
        num += b[j]
print(num)
