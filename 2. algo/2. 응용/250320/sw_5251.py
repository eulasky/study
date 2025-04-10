import heapq

def dijkstra(st):
    pq = [(0, st)]
    dists = [INF] * (N+1)
    dists[st] = 0

    while pq:
        d, n = heapq.heappop(pq)

        if dists[n] < d:
            continue

        for next_info in graph[n]:
            next_d = next_info[0]
            next_n = next_info[1]

            new_d = d + next_d

            if new_d >= dists[next_n]:
                continue

            dists[next_n] = new_d

            heapq.heappush(pq, (new_d, next_n))

    return dists[-1]

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    INF = int(21e8)

    st = 0
    graph = [[] for _ in range(N+1)]

    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((w, e))

    result = dijkstra(0)
    print(f'#{tc} {result}')
