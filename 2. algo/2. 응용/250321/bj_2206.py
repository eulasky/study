# import sys
# sys.stdin = open("maps.txt", "r")
from collections import deque

def bfs(i, j, check):
    global min_cnt
    visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
    q = deque()
    q.append((i, j, check))
    visited[i][j][0] = 1

    while q:
        ci, cj, check = q.popleft()

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci+di, cj+dj

            if ni < 0 or ni >= N or nj < 0 or nj >= M:
                continue

            if visited[ni][nj][0] == 0 and check == 0:
                if maps[ni][nj] == 0:
                    q.append((ni, nj, 0))
                    visited[ni][nj][0] = visited[ci][cj][0] + 1
                if maps[ni][nj] == 1:
                    q.append((ni, nj, 1))
                    visited[ni][nj][1] = visited[ci][cj][0] + 1

            elif visited[ni][nj][1] == 0 and check == 1:
                if maps[ni][nj] == 0:
                    q.append((ni, nj, 1))
                    visited[ni][nj][1] = visited[ci][cj][1] + 1

    result = min(visited[N-1][M-1])
    if result == INF:
        result = -1

    return result
    # result = min(-visited[-1][-1][0], -visited[-1][-1][1], -1)
    # return -result if result >= 0 else result

N, M = map(int, input().split())
maps = [list(map(int, input())) for _ in range(N)]
result = bfs(0, 0, 0)
print(bfs(0, 0, 0))