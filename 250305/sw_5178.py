def post_order(n, N):
    if n <= N:
        if TREE[n] == 0:
            l = post_order(n * 2, N)
            r = post_order(n * 2 + 1, N)
            TREE[n] = l+r

        return TREE[n]

    return 0

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    TREE = [0]*(N+1)

    for _ in range(M):
        node, number = map(int, input().split())
        TREE[node] = number

    post_order(1, N)
    print(f'#{tc} {TREE[L]}')