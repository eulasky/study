import sys
sys.stdin = open("sw_2105.txt", "r")

dy = [1, 1, -1, -1, 0]
dx = [1, -1, -1, 1, 0]

def tour(row, col, s, d):
    global max_dessert

    if d > 3:
        if sti == row and stj == col:
            max_dessert = max(s, max_dessert)
        return

    # if sti == row and stj == col:
    #     max_dessert = max(s, max_dessert)



    nr, nc = row+dy[d], col+dx[d]
    if 0 <= nr < N and 0 <= nc < N and kind[dessert[nr][nc]] == 0:
        kind[dessert[nr][nc]] = 1
        tour(nr, nc, s+1, d)
        tour(nr, nc, s+1, d+1)
        kind[dessert[nr][nc]] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    dessert = [list(map(int, input().split())) for _ in range(N)]
    max_dessert = -1

    for row in range(N):
        for col in range(N):
            kind = [0] * 101
            sti, stj = row, col
            tour(row, col, 0, 0)

    max_dessert = -1 if max_dessert == 0 else max_dessert

    print(f'#{tc} {max_dessert}')