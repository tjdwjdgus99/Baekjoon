# -*- coding: utf-8 -*-

n = int(input())
s = []

for i in range(n):
    one,two = map(int,input().split())
    s.append([one,two])

s = sorted(s,key=lambda x:(x[1] , x [0]))#앞자리를 먼저 기준으로 정렬 후 다시 뒷자리를 기준으로 정렬
last = 0
cnt = 0
for i , j in s:
    if i >=last:
        cnt += 1
        last = j
print(cnt)
