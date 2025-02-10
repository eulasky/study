def getValue():

    return value

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[-1] * N for _ in range(N)]
    delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    d = 0
    row = col = 0
    value = 1

    for i in range(1, N*N +1):
        # value = getValue()  # 무슨 value지...
        arr[row][col] == i
        newR = row + delta[d][0]
        newC = col + delta[d][1]
        if newR < 0 or newR >= N or newC < 0 or newC >= N or arr[newR][newC] != -1:
            # d = d+1
            # if d == 4:
            #      d == 0
            d = (d+1) % 4

        row += delta[d][0]
        col += delta[d][1]

    print(arr)