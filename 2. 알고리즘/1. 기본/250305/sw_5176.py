def in_order(n, N):
    global k
    if n <= N:
        in_order(n * 2, N)
        tree[n] = k
        k += 1
        in_order(n*2+1, N)







T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    k = 1

    in_order(1, N)
    print(tree)

    print(f'#{tc} {tree[1]} {tree[N//2]}')