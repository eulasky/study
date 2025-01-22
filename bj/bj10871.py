N, X = map(int, input().split())
A = []

for _ in range(1, N+1):
    i = int(input())
    A.append(i)

for i in A:
    if j < X:
        print(j, end=' ')