# -*- coding: utf-8 -*-

name = list(input())

start = 'A'
time = 0

for i in name:
    left = ord(i) - ord(start)#ord는 아스키 코드로 만들어줌
    rigth = ord(start) - ord(i)

    if left < 0:#-로 되어있는 수를 +로 만들어줌
        left += 26
    elif rigth < 0:
        rigth += 26

    time += min(left,rigth)
    start = i

print(time)