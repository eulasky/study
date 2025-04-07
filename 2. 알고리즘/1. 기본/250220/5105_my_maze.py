def find_st(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                return i, j

def dfs(i, j, N):
    visited = [[0] * N for _ in range(N)]   # visited 생성
    q = []                                  # 큐 생성
    q.append((i, j))                        # 시작점 인큐
    visited[i][j] = 1                       # 시작점 인큐 표시
    while q:                                # q에 원소가 있는 동안
        ti, tj = q.pop(0)                   # t 시작
        if maze[ti][tj] == 3:
            return visited[ti][tj] - 2

        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            wi, wj = ti+di, tj+dj
            if 0 <= wi < N and 0 <= wj < N and maze[wi][wj] != 1 and visited[wi][wj] == 0:
                q.append((wi, wj))
                visited[wi][wj] = visited[ti][tj] + 1
    return 0




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]


    sti, stj = find_st(maze)
    ans = dfs(sti, stj, N)

    print(f'#{tc} {ans}')