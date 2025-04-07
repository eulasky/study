def dfs(node):
    visited[node] = 1

    for i in graph[node]:
        if not visited[i]:
            dfs(i)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    nodes = list(map(int, input().split()))
    visited = [0] * (N+1)

    for i in range(M):
        graph[nodes[i*2]].append(nodes[i*2+1])
        graph[nodes[i*2+1]].append(nodes[i*2])

    cnt = 0
    for j in range(1, N+1):
        if not visited[j]:
            dfs(j)
            cnt += 1

    print(f'#{tc} {cnt}')