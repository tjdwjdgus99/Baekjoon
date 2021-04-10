# -*- coding: utf-8 -*-

T = int(input(''))#총 샘플 갯수

for i in range(T):
    N = int(input(''))#원소의 갯수
    card_list = input('').split()#원소

    min_card = card_list[0]#처음값=최솟값
    res_list = [card_list[0]]#출력할 리스트

    for j in range(1, N):
        if min_card >= card_list[j]:#최솟값보다 작으면
            min_card = card_list[j]#최솟값으로 만들어주기
            res_list.insert(0, card_list[j])#0번째 자리에 최솟값넣어주기
                                           #자리가 차있으면 0부터 한칸씩 밀어냄
        else:
            res_list.append(card_list[j])#아니면 순서대로 넣기

    for j in range(N):#하나씩 출력
        print(res_list[j], end='')#최솟값들을 출력해주고