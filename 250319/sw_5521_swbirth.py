def bff(node):
    q = [node]
    visited[node] = 1
    cnt = 0

    while q:
        c = q.pop(0)
        if 1 < visited[c] <= 3:
            cnt += 1
        if visited[c] > 3:
            return cnt

        for i in friends[c]:
            if not visited[i]:
                q.append(i)
                visited[i] = visited[c] + 1
    return 0

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    friends = [[] for _ in range(N+1)]
    visited = [0] * (N+1)

    for _ in range(M):
        a, b = map(int, input().split())
        friends[a].append(b)
        friends[b].append(a)

    print(f'#{tc} {bff(1)}')