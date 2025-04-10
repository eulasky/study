T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    color_count = [[0] * 10 for _ in range(10)]
    for i in range(N):
        color = list(map(int, input().split()))
        for row in range(color[0], color[2] + 1):
            for col in range(color[1], color[3] + 1):
                color_count[row][col] += 1

    purple = 0
    for row in range(10):
        for col in range(10):
            if color_count[row][col] == 2:
                purple += 1

    print(f'#{test_case} {purple}')




