T = int(input())
for tc in range(1, T+1):
    N = int(input())
    truck = [list(map(int, input().split())) for _ in range(N)]

    truck_end = sorted(truck, key=lambda x:x[1])

    cnt = 1
    end = truck_end[0][1]
    for i in range(N):
        if truck_end[i][0] >= end:
            end = truck_end[i][1]
            cnt += 1

    print(f'#{tc} {cnt}')