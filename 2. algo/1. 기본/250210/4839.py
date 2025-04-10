def bin_search(n, a):
    l = 1
    r = n
    cnt = 0
    while l <= r:
        c = int((l + r) / 2)
        if c == a:
            cnt += 1
            return cnt
        elif c > a:
            r = c
            cnt += 1
        else:
            l = c
            cnt += 1
    return cnt


T = int(input())

for tc in range(1, T+1):
    P, A, B = map(int, input().split())

    A_cnt = bin_search(P, A)
    B_cnt = bin_search(P, B)

    if A_cnt > B_cnt:
        winner = 'B'
    elif A_cnt < B_cnt:
        winner = 'A'
    else:
        winner = 0

    print(f'#{tc} {winner}')

