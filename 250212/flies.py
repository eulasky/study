T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]

    max_sum = 0
    for row in range(N):
        for col in range(N):
            cur_max = 0
            sum1 = flies[row][col]
            for j in range(1, M):
                for di, dj in [(0, j), (j, 0), (-j, 0), (0, -j)]:
                    ni, nj = row + di, col + dj
                    if 0 <= ni < N and 0 <= nj < N:
                        sum1 += flies[ni][nj]

            sum2 = flies[row][col]
            for k in range(1, M):
                for di, dj in [(k, k), (k, -k), (-k, k), (-k, -k)]:
                    ni, nj = row + di, col + dj
                    if 0 <= ni < N and 0 <= nj < N:
                        sum2 += flies[ni][nj]

            if sum1 > sum2:
                cur_max = sum1
            else:
                cur_max = sum2

            if max_sum < cur_max:
                max_sum = cur_max

    print(f'#{tc} {max_sum}')


