# -*- coding: utf-8 -*-

n = int(input())

x, y = map(int, input().split())#첫번째 입력받고

result = 0
for i in range(n-1):
    xx, yy = map(int,input().split())#그다음것들 계속 입력받기
    if xx == x:#x가 그다음꺼랑 이번꺼랑 같으면
        y = yy#y는 이번껄 다음꺼로 바꾸어준다
    elif y>=xx and yy>y:#다음x보다 y가 크거나 같고 다음y가 지금y보다 크면
        y = yy#y는 이번껄 다음꺼로 바꾸어준다
    elif y<xx:#지금y가 다음 x보다 작으면
        result += abs(x-y)#절대값
        x = xx
        y = yy

print(result+abs(y-x))