T = int(input())

for tc in range(1, T+1):
    N = int(input())
    origin = list(map(int, input().split()))
    result = list(map(int, input().split()))

    cnt = 0
    for i in range(N):
        if origin[i] != result[i]:
            cnt += 1
            for j in range(i, N):
                origin[j] = (origin[j]+1)%2


    print(f'#{tc} {cnt}')