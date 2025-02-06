T = int(input())

for test_case in range(1, T+1):
    K, N, M = map(int, input().split())
    charges = list(map(int, input().split()))
    bus_path = [0] * (N+K+2)

    for charge in charges:
        bus_path[charge] = 1    # 버스 정류장 있는 곳 표시


    bus_path[N] = 1
    bus_now = 0
    charge_count = 0
    while bus_now < N:
        charge_path_count = 0
        for i in range(bus_now + 1, bus_now + K + 1):
            if bus_path[i] == 1:
                bus_now = i
                charge_path_count += 1

        if charge_path_count == 0:
            charge_count = 1
            break
        else:
            charge_count += 1

    print(f'#{test_case} {charge_count-1}')



