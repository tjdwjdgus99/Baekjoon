# -*- coding: utf-8 -*-

N = int(input())
a = list(map(int,input().split()))
b = sorted(a)
c = []
for i in range(N):
    idx = b.index(a[i])#인덱스를 받아서
    c.append(idx)#넣어주고
    b[idx] =- 1#하나씩 빼주기

print(*c)#*는 리스트를 해체시켜줌