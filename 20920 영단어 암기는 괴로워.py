# -*- coding: utf-8 -*-

n , a = (map(int, input().split()))#map 함수를 이용해 각각 객체로 만듬
words = []

for i in range(n):
    words.append(input())
for i in range(n):
    if len(words[i]) < a:
        words.remove(words[i])
    elif len(words[i]) >= a:
        continue
print[words]
#실패함-----------------------------