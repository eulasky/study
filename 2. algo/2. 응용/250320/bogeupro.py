import heapq

def min_time(si, sj):
    pq = [(0, si, sj)]
    time = [[INF] * N for _ in range(N)]
    time[si][sj] = 0

    while pq:
        depth, ci, cj = heapq.heappop(pq)

        if time[ci][cj] < depth:
            continue

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci+di, cj+dj

            if 0 <= ni < N and 0 <= nj < N:
                depth_total = time[ci][cj] + area[ni][nj]

                if depth_total >= time[ni][nj]:
                    continue

                time[ni][nj] = depth_total
                heapq.heappush(pq, (depth_total, ni, nj))

    return time[-1][-1]

T = int(input())
for C in range(1, T+1):
    N = int(input())
    area = [list(map(int, input())) for _ in range(N)]
    INF = int(21e8)

    result = min_time(0, 0)

    print(f'#{C} {result}')
