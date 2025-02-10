T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    d = 0
    row = col = 0

    for i in range(1, N*N+1):
        arr[row][col] = i
        newR = row + dir[d][0]
        newC = col + dir[d][1]

        if newR < 0 or newR >= N or newC < 0 or newC >= N or arr[newR][newC] != 0:
            d = (d+1) % 4

        row += dir[d][0]
        col += dir[d][1]

    print(arr)


