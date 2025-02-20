def dfs(s):
    global N
    stack = []
    visited = [0] * (N + 1)
    stack.append(s)
    visited[s] = 1
    while stack:
        t = stack.pop()
        for i in bg[t]:
            if visited[i] == 0:
                stack.append(i)
                visited[i] = 1
    stack.append(s)
    while stack:
        t = stack.pop()
        for j in sg[t]:
            if visited[j] == 0:
                stack.append(j)
                visited[j] = 1

    if sum(visited) == N:
        return 1
    else:
        return 0


N, M = map(int, input().split())
bg = [[] for _ in range(N + 1)]
sg = [[] for _ in range(N + 1)]

for _ in range(M):
    g = list(map(int, input().split()))
    bg[g[0]].append(g[1])
    sg[g[1]].append(g[0])

cnt = 0
for k in range(1, N + 1):
    cnt += dfs(k)

print(cnt)