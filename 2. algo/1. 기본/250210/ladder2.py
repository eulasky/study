T = 10
for _ in range(T):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    min_cnt = 0 ### 이거라 틀림림
    for col in range(100):
        if ladder[0][col] == 1:
            cnt = 0
            for row in range(100):
                if col-1 >=0 and ladder[row][col-1] == 1:
                    while col-1>=0 and ladder[row][col-1] == 1:
                        col -= 1
                        cnt += 1
                if col+1 < 100 and ladder[row][col+1] == 1:
                    while col+1 < 100 and ladder[row][col+1] == 1:
                        col += 1
                        cnt += 1

            if min_cnt > cnt:
                min_cnt = cnt
    print(f'#{tc} {min_cnt}')
