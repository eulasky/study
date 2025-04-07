def solve():
    result = []
    q = []
    for i in range(1, V+1):
        if IN[i] == 0:
            q.append(i)

    while q:
        v = q.pop(0)
        result.append(v)

        for i in range(V+1):
            if G[v][i]:
                IN[i] -= 1
                if IN[i] == 0:
                    q.append(i)
    return result

T = 10
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = list(map(int, input().split()))

    G = [[0] * (V+1) for _ in range(V+1)]
    IN = [0] * (V+1)
    for i in range(0, len(arr), 2):
        st = arr[i]
        ed = arr[i+1]
        G[st][ed] = 1
        IN[ed] += 1

    result = solve()
    print(f'#{tc}', *result)