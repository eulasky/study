def find_s(arr):
    for row in range(16):
        for col in range(16):
            if maze[row][col] == 2:
                return (row, col)
def find_g(sr, sc):
    visited = [[0]*100 for _ in range(100)]
    q = []
    q.append((sr, sc))
    visited[sr][sc] = 1

    while q:
        cr, cc = q.pop(0)
        if maze[cr][cc] == 3:
            return 1

        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = cr+di, cc+dj
            if 0 <= ni < 100 and 0 <= nj < 100 and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = 1
    return 0


T = 10
for _ in range(1, T+1):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(100)]

    si, sj = find_s(maze)
    result = find_g(si, sj)

    print(f'#{tc} {result}')

