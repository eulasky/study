T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    space = [list(map(int, input().split())) for _ in range(N)]

    max_die = 0
    for row in range(N-M+1):
        for col in range(N-M+1):
            fly_die = 0
            for row2 in range(M):
                for col2 in range(M):
                    fly_die += space[row + row2][col + col2]

            if max_die < fly_die:
                max_die = fly_die

    print(f'#{test_case} {max_die}')

