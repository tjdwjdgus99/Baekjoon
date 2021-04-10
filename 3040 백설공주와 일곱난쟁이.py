# -*- coding: utf-8 -*-

a = []
for i in range(9): #9번 반복
    a.append(int(input())) #마지막 자리에 입력받는다
add = sum(a) #합
a.sort() #정렬

for i in range(9):
    for j in range(i+1,9):
        if add - a[i]-a[j]==100:#있으면 안되는 숫자를 찾아서
            for k in range(9):
                if k==i or k==j: continue#그 숫자들을 빼고
                else:
                    print(a[k])#출력
            exit()