def pre_order(n):
    global cnt
    if n:
        cnt += 1
        pre_order(L[n])
        pre_order(R[n])


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    nodes = list(map(int, input().split()))
    V = E+1
    L = [0] * (V+1)
    R = [0] * (V+1)
    cnt = 0


    for i in range(E):
        p, c = nodes[i*2], nodes[i*2+1]
        if L[p] == 0:
            L[p] = c
        else:
            R[p] = c

    pre_order(N)
    print(f'#{tc} {cnt}')

