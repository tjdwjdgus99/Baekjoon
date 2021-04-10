# -*- coding: utf-8 -*-

n = int(input())
a = list(map(int,input().split()))#도로 길이
b = list(map(int,input().split()))#도시 기름값
count = a[0] * b[0]#가격
m = b[0]
dist = 0

for i in range(1 , n-1):#첫번째 도시에선 무조건 기름을 채워야함
    if b[i] < m:#다음 도시기름값이 지금 도시기름값 보다 싸면
        count += m * dist
        dist = a[i]#주유가격 변경
        m = b[i]#주유가격 변경
    else:#아니면 계속 그가격 유지하면서 돈계산
        dist += a[i]
    if i == n-2:#마지막 도로에서 넘어갈때 가격계산
        count += m * dist
print(count)