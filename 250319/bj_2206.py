def bfs(i, j, check):
    visited = [[0]*M for _ in range(N)]
    q = []
    q.append((i, j, check))
    visited[i][j] = 0

    while q:
        ci, cj, check = q.pop(0)

        if ci == N-1 and cj == M-1:
            return visited[ci][cj]


        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and maps[ni][nj] == 0 and check == 0:
                q.append((ni, nj, 0))
                visited[ni][nj] = visited[ni][nj] + 1
            elif 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and maps[ni][nj] == 1 and check == 0:
                check = 1
                q.append((ni, nj, 1))
                visited[ni][nj] = visited[ni][nj] + 1
            elif 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and maps[ni][nj] == 0 and check == 1:
                q.append((ni, nj, 1))
                visited[ni][nj] = visited[ni][nj] + 1

    return -1

N, M = map(int, input().split())
maps = [list(map(int, input())) for _ in range(N)]
print(bfs(0, 0, 0))

