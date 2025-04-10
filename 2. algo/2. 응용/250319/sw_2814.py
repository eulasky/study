import sys
sys.stdin = open("maxlen.txt", "r")

def dfs(node, cnt):
    global max_v
    visited[node] = 1
    max_v = max(max_v, cnt)

    for i in graph[node]:
        if not visited[i]:
            dfs(i, cnt+1)
    visited[node] = 0

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    visited = [0] * (N+1)
    max_v = 0

    for _ in range(M):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)

    for j in range(1, N+1):
        dfs(j, 1)

    print(f'#{tc} {max_v}')
