n =int(input())

for i in range(n):
    A, B = map(int, input().split())
    a, b = A, B

    while b != 0:
        a = a % b
        a, b = b, a

    print(A * B // a)
