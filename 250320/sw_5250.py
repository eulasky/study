def dijkstra(si, sj):
    pq = [(0, si, sj)]          # 누적거리, 좌표
    charge = [[INF] * N for _ in range(N)] # 각 정점까지의 최소 연료를 저장할 리스트
    charge[si][sj] = 0           # 시작 노드 최단거리는 0

    while pq:
        gas, ci, cj = heapq.heappop(pq)

        if charge[ci][cj] < gas:
            continue

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci+di, cj+dj

            if 0 <= ni < N and 0 <= nj < N:
                diff = max(area[ni][nj]-area[ci][cj], 0) + 1
                new_gas = charge[ci][cj] + diff

                if new_gas >= charge[ni][nj]:
                    continue

                charge[ni][nj] = new_gas
                heapq.heappush(pq, (new_gas, ni, nj))

    return charge[-1][-1]

import heapq

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]
    INF = int(21e8)

    result = dijkstra(0, 0)

    print(f'#{tc} {result}')

