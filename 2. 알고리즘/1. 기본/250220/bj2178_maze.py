def min_maze(str, stc, gr, gc):
    visited = [[0]*M for _ in range(N)]
    q = []
    q.append((str, stc))
    visited[str][stc] = 1
    while q:
        vi, vj = q.pop(0)
        if vi == gr and vj == gc:
            return visited[vi][vj]

        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            wi, wj = vi+di, vj+dj
            if 0 <= wi < N and 0 <= wj < M and maze[wi][wj] == 1 and visited[wi][wj] == 0:
                q.append((wi, wj))
                visited[wi][wj] = visited[vi][vj] + 1

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

sti = stj = 0
gi, gj = (N-1), (M-1)

print(min_maze(sti, stj, gi, gj))