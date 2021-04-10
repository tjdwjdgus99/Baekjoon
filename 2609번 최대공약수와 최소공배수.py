A , B = map(int, input().split()) # 유클리드 호제법을 사용해 풀기
a, b = A, B

while b != 0:
    a = a % b
    a, b = b, a

print(a)#최대공약수

print(A*B//a)#최소공배수