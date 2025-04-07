def dfs(s):
    global N
    stack = []
    visited = [0] * (N + 1)

    while 1:
        if visited[s] == 0:
            visited[s] = 1

        for w in bg[s]:
            if visited[w] == 0:
                stack.append(v)
                v = w
                break
        else:
            if stack:
                v = stack.pop()
            else:
                break


N, M = map(int, input().split())
bg = [[] for _ in range(N+1)]
sg = [[] for _ in range(N+1)]

for _ in range(M):
    g = list(map(int, input().split()))
    bg[g[0]].append(g[1])
    sg[g[1]].append(g[0])

