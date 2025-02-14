def dfs(v, e):
    visited = [0] * (V+1)
    STACK = []

    while v != e:
        if visited[v] == 0:
            visited[v] = 1

        for w in adj[v]:
            if visited[w] == 0:
                STACK.append(v)
                v = w
                break
        else:
            if STACK:
                v = STACK.pop()
            else:
                return 0
    return 1



T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(E)]
    adj = [[] for _ in range(V+1)]

    for i in graph:
        adj[i[0]].append(i[1])

    S, G = map(int, input().split())

    result = dfs(S, G)

    print(f'#{tc} {result}')
