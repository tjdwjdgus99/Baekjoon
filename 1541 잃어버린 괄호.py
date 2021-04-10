a = input().split('-')#55 - 50 + 40 - 30 + 20입력 받으면
                      #['55', '50 + 40', '30 + 20']이렇게 바꾸어준다
num = []
for i in a:#a번 반복해주고
    cnt = 0
    s = i.split('+')#+를 기준으로 나누어준다
    for j in s:#s번 반복해주고
        cnt += int(j)#안의 +기준으로 있는것들을 더해주고
    num.append(cnt)#차례로 줄세워준다
n = num[0]
for i in range(1,len(num)):
    n -= num[i]#마지막으로 빼주면
print(n)