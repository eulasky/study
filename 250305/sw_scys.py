def post_order(n):
    if n:
        a = post_order(L[n])
        b = post_order(R[n])

        if TREE[n] == '+':
            TREE[n] = a + b
        elif TREE[n] == '-':
            TREE[n] = a - b
        elif TREE[n] == '*':
            TREE[n] = a * b
        elif TREE[n] == '/':
            TREE[n] = a // b

        return TREE[n]





T = 10
for tc in range(1, T+1):
    N = int(input())
    cal = [input().split() for _ in range(N)]
    TREE = [0]*(N+1)
    L = [0]*(N+1)
    R = [0]*(N+1)

    for i in range(N):
        if len(cal[i]) == 4:
            TREE[int(cal[i][0])] = cal[i][1]
            L[int(cal[i][0])] = int(cal[i][2])
            R[int(cal[i][0])] = int(cal[i][3])
        elif len(cal[i]) == 2:
            TREE[int(cal[i][0])] = int(cal[i][1])


    post_order(1)
    print(f'#{tc} {TREE[1]}')

