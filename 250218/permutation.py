def per_1(k):
    if k == N:
        print(result)
        return

    candidates = []
    for i in range(N):
        if i not in result[0:k]:
            candidates.append(i)
    for i in candidates:
        result[k] = i
        per_1(k+1)


def per(k):
    if k == N:
        print(result)
        return

    for i in range(N):
        if not visited[i]:
            result[k] = i
            visited[i] = True
            per(k+1)
            visited[i] = False


N = 5
arr = [1, 41, 23, 12, 26]

result = [-1] * N
visited = [False] * N

per_1()