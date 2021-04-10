# -*- coding: utf-8 -*-

n = int(input())
arr = list(map(int,input().split()))
ans = 0

for i in range(n):
    if arr[i] == 1:
        ans += 1
        for j in range(3):#켜진 것과 오른쪽 2개를 누르기
            if i + j < n:#최댓값을 넘기지 않도록
                if arr[i + j] == 0:
                    arr[i + j] = 1
                else: arr[i + j] = 0
print(ans)