def bfs(s, g, v):
    visited = [0] * (v+1)
    q = []
    q.append(s)
    visited[s] = 1
    while q:
        t = q.pop(0)
        if t == g:
            return visited[t] - 1

        for i in adj_l[t]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[t] + 1
    return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj_l = [[] for _ in range(V+1)]

    for _ in range(E):
        v1, v2 = map(int, input().split())
        adj_l[v1].append(v2)
        adj_l[v2].append(v1)

    S, G = map(int, input().split())

    print(f'#{tc} {bfs(S, G, V)}')


