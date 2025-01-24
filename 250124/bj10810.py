N, M = map(int, input().split())
result_list = [0] * N

for cnt1 in range(M):
    i, j, k = map(int, input().split())
    if k <= N:
        for cnt2 in range(i-1, j):
            result_list[cnt2] = k
    
print(*result_list)



