def cytown(person):
    visited[person] = 1

    for i in myfriend[person]:
        if not visited[i]:
            cytown(i)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    myfriend = [[] for _ in range(N+1)]
    visited = [0] * (N+1)

    for _ in range(M):
        a, b = map(int, input().split())
        myfriend[a].append(b)
        myfriend[b].append(a)

    cnt = 0
    for i in range(1, N+1):
        if not visited[i]:
            cytown(i)
            cnt += 1

    print(f'#{tc} {cnt}')
