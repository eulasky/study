def dfs(v, e):
    visited = [0] * (100+1)
    STACK = []

    while v != e:
        if visited[v] == 0:
            visited[v] = 1

        for w in new_graph[v]:
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



T = 10

for _ in range(1, T+1):
    tc, path = map(int, input().split())
    graph = list(map(int, input().split()))
    adj1 = [-1] * 100
    adj2 = [-1] * 100

    for i in range(0, len(graph), 2):
        if adj1[graph[i]] == -1:
            adj1[graph[i]] = graph[i+1]
        else:
            adj2[graph[i]] = graph[i+1]

    new_graph = list(zip(adj1, adj2))

    result = dfs(0, 99)

    print(f'#{tc} {result}')
