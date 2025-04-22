def change(k, charge, cnt):
    global min_cnt
    if charge < 0:
        return
    if min_cnt <= cnt:
        return
    if k+charge >= N-1:
        min_cnt = min(cnt, min_cnt)
    if k == N-1:
        return

    change(k+1, battery[k]-1, cnt+1)
    change(k+1, charge-1, cnt)


T = int(input())
for tc in range(1, T+1):
    N, *battery = map(int, input().split())

    min_cnt = N+1

    change(0, battery[0], 0)

    print(f'#{tc} {min_cnt}')
