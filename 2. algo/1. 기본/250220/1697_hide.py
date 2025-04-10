def hide(n, k):
    visited = [0] * 100001
    q = []
    q.append(n)
    visited[n] = 1
    while q:
        t = q.pop(0)
        if t == k:
            return visited[t] - 1

        for i in [t-1, t+1, t*2]:
            if 0 <= i < 100001 and visited[i] == 0:
                q.append(i)
                visited[i] = visited[t] + 1

N, K = map(int, input().split())

print(hide(N, K))

