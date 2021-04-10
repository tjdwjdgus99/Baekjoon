# -*- coding: utf-8 -*-

p = [1,2]#2번째 3번째 자리
for i in range(2,46):
    p.append(p[i-2] + p[i-1])#피보나치 수열 만들어 놓기
T = int(input())#갯수

for j in range(T):
    n = int(input())
    result = []

    while(n):#0일때 까지 반복
        for k in range(46):#피보나치 수열 46개
            if(p[k] <= n):#n에 최고 근접한걸 찻아서
                t = p[k]
        n -= t#n을 빼준다
        result.append(t)
        result.sort()#정렬후
    for b in range(len(result)):#결과값 출력
        print(result[b], end=' ')#한칸씩 뛰어서
