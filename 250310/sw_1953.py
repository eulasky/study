def pos(N, M, R, C, L):
    connect = {
        1:[(-1, 0), (1, 0), (0, -1), (0, 1)],
        2:[(-1, 0), (1, 0)],
        3:[(0, -1), (0, 1)],
        4:[(-1, 0), (0, 1)],
        5:[(1, 0), (0, 1)],
        6:[(1, 0), (0, -1)],
        7:[(-1, 0), (0, -1)]
    }

    visited = [[0]*M for _ in range(N)]
    q = []
    q.append((R, C))
    visited[R][C] = 1
    cnt = 1

    while q:
        ci, cj = q.pop(0)
        # if visited[ci][cj] == L:
            # return cnt

        for di, dj in connect[tunnel[ci][cj]]:
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < M and tunnel[ni][nj] != 0 and visited[ni][nj] == 0 and visited[ci][cj] < L:
                reverse = (di * (-1), dj * (-1))
                if reverse in connect[tunnel[ni][nj]]:
                    q.append((ni, nj))
                    visited[ni][nj] = visited[ci][cj] + 1
                    cnt += 1
    return cnt

T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]

    result = pos(N, M, R, C, L)
    print(f'#{tc} {result}')
