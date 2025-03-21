def order(node):
    for c in graph[node]:
        if visited[c] == 0:
            order(c)

    visited[node] = 1
    path.append(node)

T = 10
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    nodes = list(map(int, input().split()))
    visited = [0] * (V+1)
    path = []

    for i in range(E):
        graph[nodes[i*2+1]].append(nodes[i*2])

    for i in range(1, V+1):
        if visited[i] == 0:
            order(i)

    print(f'#{tc}', *path)
