def dfs(i, j, cnt, check):
    global max_cnt

    visited[i][j] = 1
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni, nj = i+di, j+dj
        if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
            if maps[i][j] > maps[ni][nj]:
                dfs(ni, nj, cnt+1, check)
            elif maps[i][j] <= maps[ni][nj] and maps[ni][nj] - maps[i][j] < K and check == 0:
                temp = maps[ni][nj]
                maps[ni][nj] = maps[i][j] - 1
                dfs(ni, nj, cnt+1, 1)
                maps[ni][nj] = temp

    max_cnt = max(max_cnt, cnt)
    visited[i][j] = 0

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    peaks = []
    max_cnt = 0

    mh = 0
    for row in range(N):
        mh = max(max(maps[row]), mh)

    for row in range(N):
        for col in range(N):
            if maps[row][col] == mh:
                peaks.append((row, col))

    for peak in peaks:
        i, j = peak
        dfs(i, j, 1, 0)

    print(f'#{tc} {max_cnt}')