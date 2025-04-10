N = int(input())

stairs = [[0]*10 for _ in range(N+1)]

for i in range(1, 10):
    stairs[1][i] = 1

for j in range(2, N+1):
    for k in range(10):
        if k == 0:
            stairs[j][k] = stairs[j-1][k+1]
        elif k == 9:
            stairs[j][k] = stairs[j-1][k-1]
        else:
            stairs[j][k] = stairs[j-1][k-1] + stairs[j-1][k+1]

result = sum(stairs[N])%1000000000

print(result)