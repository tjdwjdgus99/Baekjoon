# -*- coding: utf-8 -*-

a , b = (map(int, input().split()))
c = []
add = 0

for i in range(a):
    c.append(input())
for i in range(a - 1,-1,-1):#a-1 부터 -1까지 -1한다
    #    반복문 시작점,끝점,건너뛸숫자 EX)3이면 3개씩 뛰어넘는다
    if b == 0:
        break
    if int(c[i]) > b:
        continue
    add += b // int(c[i])
    b %= int(c[i])
print(add)