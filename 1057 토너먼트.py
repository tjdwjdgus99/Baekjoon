# -*- coding: utf-8 -*-

n,a,b = map(int,input().split())
count = 0

while a != b:#둘이 만날때 까지
    a -= a // 2#몫
    b -= b // 2#몫
    count +=1
print(count)
