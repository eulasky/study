def electric_bus(k, charge, cnt):
    global min_cnt

    if charge < 0:
        return
    if min_cnt < cnt:
        return
    if k+charge >= N-1:
        min_cnt = min(min_cnt, cnt)
        return
    if k == N-1:
        return

    electric_bus(k+1, charge-1, cnt)
    electric_bus(k+1, battery[k]-1, cnt+1)

T = int(input())
for tc in range(1, T+1):
    N, *battery = map(int, input().split())
    min_cnt = N+1

    electric_bus(0, battery[0], 0)

    print(f'#{tc} {min_cnt}')