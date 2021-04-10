# -*- coding: utf-8 -*-

a = int(input())

for i in range(a):
    n = int(input())
    trees=list(map(int,input().split()))
    trees.sort()
    result=0
    for j in range(2,n):
        result = max(result,abs(trees[j]-trees[j-2]))#절대값중 가장큰걸 출력
    print(result)