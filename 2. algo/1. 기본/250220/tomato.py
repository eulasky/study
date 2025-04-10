def ripen(arr):
    tr = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                tr.append((i, j))
                return tr

def ref():
    while q:
        ci, cj = q.pop(0)
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            wi, wj = ci+di, cj+dj
            if 0 <= wi < N and 0 <= wj < M and tomato[wi][wj] == 0 and visited[wi][wj] == 0:
                q.append((wi, wj))
                visited[wi][wj] = visited[ci][cj] + 1

    return visited[wi][wj]






M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
q = []

tomatoes = ripen(tomato)
for ti, tj in tomatoes:
    q.append((ti, tj))
    visited[ti][tj] = 1
    print(q)

print(ref())

