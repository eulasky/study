T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]

    max_die = 0
    for row in range(N-M+1):
        for col in range(N-M+1):
            flies_die = 0
            for row2 in range(M):
                for col2 in range(M):
                    flies_die += flies[row+row2][col+col2]
            if max_die < flies_die:
                max_die = flies_die
    print(f'#{tc} {max_die}')