# -*- coding: utf-8 -*-

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
result = 0

A.sort(reverse=True)#높은수 부터 정렬
B.sort()

for i in range(N):
    result += A[i] * B[i]

print(result)