T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    pic = [list(map(int, input().split())) for _ in range(N)]

    # 행 탐색
    max_len = 0
    for row in range(N):
        len = 0
        for col in range(M):
            if pic[row][col] == 1:
                len += 1
                if max_len < len:
                    max_len = len
            else:
                len = 0
        # if max_len < len:
        #     max_len = len

    # 열 탐색
    for col in range(M):
        len = 0
        for row in range(N):
            if pic[row][col] == 1:
                len += 1
            else:
                if max_len < len:
                    max_len = len
                len = 0
        if max_len < len:
            max_len = len

    print(f'#{tc} {max_len}')



