def in_order(n):
    global result
    if n:
        in_order(L[n])
        result += TREE[n]
        in_order(R[n])

T = 10

for tc in range(1, T+1):
    N = int(input())
    TREE = [0] * (N+1)
    L = [0] * (N+1)
    R = [0] * (N+1)
    data = [input().split() for _ in range(N)]
    result = ''

    for i in range(N):
        if len(data[i]) >= 2:
            TREE[int(data[i][0])] = data[i][1]
        if len(data[i]) >= 3:
            L[int(data[i][0])] = int(data[i][2])
        if len(data[i]) == 4:
            R[int(data[i][0])] = int(data[i][3])

    in_order(1)
    print(f'#{tc} {result}')



