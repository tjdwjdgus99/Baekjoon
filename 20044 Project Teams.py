# -*- coding: utf-8 -*-

n = int(input())
team = list(map(int,input().split()))
team.sort()

answer = []
for i in range(len(team)):
    answer.append(team[i]+team[len(team) - 1 - i])

print(min(answer))

