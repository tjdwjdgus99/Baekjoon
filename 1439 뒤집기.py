# -*- coding: utf-8 -*-

a = input()
count = 0
for i in range(len(a)-1):
    if a[i] != a[i + 1]:#달라질때 마다 카운트해주고
        count += 1
print((count + 1) // 2)#2배로 카운트한걸 고쳐주기
