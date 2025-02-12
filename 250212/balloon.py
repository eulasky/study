T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    balloon = [list(map(int, input().split())) for _ in range(N)]

    max_sum = 0
    for row in range(N):
        for col in range(M):
            sum = balloon[row][col]
            i = balloon[row][col]
            for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                ni, nj = row + di, col + dj
                if 0 <= ni < N and 0 <= nj < M:
                    sum += balloon[ni][nj]
            if max_sum < sum:
                max_sum = sum

    print(f'#{tc} {max_sum}')

