n = input()
f = int(input())
a = int(n[:-2] + '00')#뒤에서 2번째 까지 잘라주고 00을 더해준다.

while True:
    if a % f == 0:#f로 나누었을때 나머지가 0이 되는 값을 찾는다.
        break
    a += 1

print(str(a)[-2:])#다시 문자열을 바꿔 뒤에서 두번째 자리부터 끝까지 잘라서 출력해준다