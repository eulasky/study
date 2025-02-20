def worm(i, j):
    q = []
    q.append((i, j))
    visited[i][j] = 1
    while q:
        si, sj = q.pop(0)
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            wi, wj = si + di, sj + dj
            if 0 <= wi < N and 0 <= wj < M and farm[wi][wj] == 1 and visited[wi][wj] == 0:
                q.append((wi, wj))
                visited[wi][wj] = 1




T = int(input())

for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    visited = [[0]*M for _ in range(N)]
    farm = [[0]*M for _ in range(N)]

    for _ in range(K):
        c, r = map(int, input().split())
        farm[r][c] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if farm[i][j] == 1 and visited[i][j] == 0:
                worm(i, j)
                cnt += 1


    print(cnt)