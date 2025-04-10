def navi(house, arr):
    pq = [(0, house)]
    dists = [10**6] * (N+1)
    dists[house] = 0

    while pq:
        dist, house = heapq.heappop(pq)

        if dists[house] < dist:
            continue

        for next_info in arr[house]:
            next_dist = next_info[0]
            next_house = next_info[1]

            new_dist = dist + next_dist

            if new_dist >= dists[next_house]:
                continue

            dists[next_house] = new_dist

            heapq.heappush(pq, (new_dist, next_house))

    return dists

import heapq

T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())
    maps1 = [[] for _ in range(N+1)]
    maps2 = [[] for _ in range(N+1)]

    for _ in range(M):
        x, y, c = map(int, input().split())
        maps1[x].append((c, y))
        maps2[y].append((c, x))

    dists1 = navi(X, maps1)
    dists2 = navi(X, maps2)

    max_time = 0
    for i in range(2, N+1):
        cur_time = dists1[i] + dists2[i]
        max_time = max(max_time, cur_time)

    print(f'#{tc} {max_time}')