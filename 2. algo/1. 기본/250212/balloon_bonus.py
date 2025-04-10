T = int(input())

for tc in range(1, T+1):
    N= int(input())
    bonus = [list(map(int, input().split())) for _ in range(N)]

    max_sum = 0
    min_sum = 360
    for row in range(N):
        for col in range(N):
            sum = bonus[row][col]
            for j in range(1, N):
                for di, dj in [(0, j), (j, 0), (-j, 0), (0, -j)]:
                    ni, nj = row + di, col + dj
                    if 0 <= ni < N and 0 <= nj < N:
                        sum += bonus[ni][nj]
            if max_sum < sum:
                max_sum = sum
            if min_sum > sum:
                min_sum = sum

    result = max_sum - min_sum
    print(f'#{tc} {result}')