def find_s(arr, N):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                return i, j

def find_g(arr, N):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 3:
                return i, j

def dfs(sti, stj, gi, gj, N):
    visited = [[0]*N for _ in range(N)]
    q = []
    q.append((sti, stj))
    visited[sti][stj] = 1
    while q:
        si, sj = q.pop(0)
        if si == gi and sj == gj:
            return 1

        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            wi, wj = si + di, sj + dj
            if 0 <= wi < N and 0 <= wj < N and maze[wi][wj] != 1 and visited[wi][wj] == 0:
                q.append((wi, wj))
                visited[wi][wj] = 1
    return 0



T = 10
for _ in range(T):
    tc = int(input())
    N = 16
    maze = [list(map(int, input())) for _ in range(N)]

    sti, stj = find_s(maze, N)
    gi, gj = find_g(maze, N)

    print(f'#{tc} {dfs(sti, stj, gi, gj, N)}')