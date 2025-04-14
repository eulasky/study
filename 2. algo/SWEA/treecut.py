import heapq

def find_start():
    for i in range(N):
        for j in range(N):
            if area[i][j] == 'X':
                return i, j

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
dirs = {0:'U', 1:'D', 2:'L', 3:'R'}

def bfs(i, j, K, field):
    pq = []
    visited = set()
    heapq.heappush(pq, (0, i, j, K, field, []))
    d = 0

    while pq:
        dist, ci, cj, K, field, path = heapq.heappop(pq)
        visited.add((ci, cj, K))

        if field[ci][cj] == 'Y':
            return path

        for d in range(4):
            ni, nj = ci+dy[d], cj+dx[d]
            if 0 > ni or N <= ni or 0 > nj or N <= nj:
                continue
            if (ni, nj, K) in visited:
                continue

            new_dist = dist + 1

            if field[ni][nj] == 'T':
                if K > 0:
                    new_path = path + ['A']
                    new_field = [row[:] for row in field]
                    new_field[ni][nj] = '.'
                    heapq.heappush(pq, (new_dist+1, ni, nj, K-1, new_field, new_path))

            elif field[ni][nj] == 'G':
                new_path = path + [dirs[d]] + ['A']
                heapq.heappush(pq, (new_dist, ni, nj, K, field, new_path))
    return -1


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    area = [list(input()) for _ in range(N)]

    si, sj = find_start()

    result = bfs(si, sj, K, area)
    print(result)

