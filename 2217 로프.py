# -*- coding: utf-8 -*-

N = int(input())
rope = []
value = []

for i in range(N):
    rope.append((int(input())))
rope.sort(reverse=True) # 정렬을 내림차순 큰 값부터 정렬

for j in range(N):
    value.append(rope[j] * (j + 1))#n번째로 큰수를 N번 곱해준다
print(max(value))