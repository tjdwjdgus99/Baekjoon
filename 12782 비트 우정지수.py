# -*- coding: utf-8 -*-

n = int(input())

for i in range(n):
    case = input('').split()
    a , b = case[0],case[1]
    one , zero = 0,0
    for j in range(len(b)):
        if a[j] == b[j]: continue#서로 같으면 넘어가고
        if b[j] == '1':
            one += 1#1갯수
        else:
            zero += 1#0갯수
    t = min(one , zero)#다른것 중에 1,0중에 작은거
    print(t + (one + zero) - t * 2)#공식찻기 ㅋㅋ