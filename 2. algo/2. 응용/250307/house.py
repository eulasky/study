import sys
sys.stdin = open("house.txt", "r")

def service(i, j, k):
    visited = [[0]*N for _ in range(N)]
    q = []
    q.append((i, j, k))
    visited[i][j] = 1
    cnt = 0
    while q:
        ci, cj, k = q.pop(0)
        if k == 0:
            break
        if city[ci][cj] == 1:
            cnt += 1

        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                q.append((ni, nj, k-1))
                visited[ni][nj] = 1

    return cnt


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]

    max_house = 0
    for row in range(N):
        for col in range(N):
            for k in range(1, N*2):
                house = service(row, col, k)
                if house*M - (k**2+((k-1)**2)) >= 0 and max_house < house:
                    max_house = house

    print(f'#{tc} {max_house}')
