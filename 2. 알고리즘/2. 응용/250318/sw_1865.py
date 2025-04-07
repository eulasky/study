def sigoto(i, N, s):
    global max_v

    if i == N:
        max_v = max(s, max_v)
        return

    for j in range(N):
        if max_v < s*arr[i][j] and visited[j] == 0:
            visited[j] = 1
            sigoto(i+1, N, s*(arr[i][j]))   # i+1 자리 결정
            visited[j] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            arr[i][j] /= 100

    visited = [0] * N
    max_v = 0
    sigoto(0, N, 1)

    print(f'#{tc} {max_v*100:.6f}')