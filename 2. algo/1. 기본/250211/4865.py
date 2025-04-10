T = int(input())

for tc in range(1, T+1):
    nl = input()
    ml = input()
    N = len(nl)
    M = len(ml)

    max_cnt = 0
    for i in range(N):
        cnt = 0
        for j in range(M):
            if nl[i] == ml[j]:
                cnt += 1
        if max_cnt < cnt:
            max_cnt = cnt

    print(f'#{tc} {max_cnt}')