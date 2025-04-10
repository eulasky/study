T = int(input())

for tc in range(1, T+1):
    N = int(input())
    pascal = [[0] * i for i in range(1, N+1)]



    for i in range(N):
        for j in range(i+1):
            if j == 0:
                pascal[i][j] = 1
            elif 0 < j < i:
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
            elif j == i:
                pascal[i][j] = 1


    print(f'#{tc}')
    for i in pascal:
        print(*i)
