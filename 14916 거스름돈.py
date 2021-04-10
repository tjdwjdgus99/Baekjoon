# -*- coding: utf-8 -*-

a = int(input())

if a in (1,3):
    result =-1
elif (a%5)%2 == 0:
    result = a//5 + (a%5)//2
else:
    result = ((a//5)-1) + ((a%5+5)//2)
print(result)
