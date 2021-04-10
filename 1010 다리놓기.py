# -*- coding: utf-8 -*-

T = int(input())

for _ in range(T):
    m, n = map(int, input().split())#mCn 공식을 이용한 풀이
    #ex)4C2 = 4!/(4-2)!/2! = 6
    answer = 1
    k = n - m

    while n > k:
        answer *= n
        n -= 1
    while m > 1:
        answer = answer // m
        m -= 1

    print(answer)




