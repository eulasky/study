def dfs(s):
    visited = [0] * (N+1)
    stack = []
    stack.append(s)
    visited[s] = 1

    while stack:
        c = stack.pop()

        for i in graph[c]:
            if visited[i] == 0:
                par[i] = c
                stack.append(i)
                visited[i] = 1


N = int(input())
par = [0] * (N+1)
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    p1, p2 = map(int, input().split())
    graph[p1].append(p2)
    graph[p2].append(p1)

dfs(1)

for i in range(2, N+1):
    print(par[i])