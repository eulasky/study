T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    word = [list(map(int, input().split())) for _ in range(N)]


    # 행 탐색
    cnt = 0
    for row in range(N):
        leng = 0
        for col in range(N):
            if word[row][col] == 1:
                leng += 1
                if col == N-1 and leng == K:
                    cnt += 1
                    leng = 0
            else:
                if leng == K:
                    cnt += 1
                    leng = 0
                else:
                    leng = 0


    # 열 탐색
    for col in range(N):
        leng = 0
        for row in range(N):
            if word[row][col] == 1:
                leng += 1
                if row == N-1 and leng == K:
                    cnt += 1
                    leng = 0
            else:
                if leng == K:
                    cnt += 1
                    leng = 0
                else:
                    leng = 0


    print(f'#{tc} {cnt}')
