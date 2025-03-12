def recur(row, col):

    if row == N-1 and col == N-1:
        print(path)
        return

    # 아래로
    if row+1 < N:
        path.append((row+1, col, arr[row+1][col]))
        recur(row+1, col)
        path.pop()

    # 오른쪽
    if col+1 < N:
        path.append((row, col+1, arr[row][col+1]))
        recur(row, col+1)
        path.pop()

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    path = [(0, 0, arr[0][0])]
    result = 10*N*N
    recur(0, 0)