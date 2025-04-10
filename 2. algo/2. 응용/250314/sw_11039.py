def garo(i, j):
    cnt = 0
    while j < N and square[i][j] != 0:
        cnt += 1
        j += 1
    return cnt

def sero(i, j):
    cnt = 0
    while i < N and square[i][j] != 0:
        cnt += 1
        i += 1
    return cnt

def visit(i, j, g, s):
    for x in range(i, i+s):
        for y in range(j, j+g):
            visited[x][y] = 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    square = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    max_area = 0
    for row in range(N):
        for col in range(N):
            if square[row][col] == 1 and visited[row][col] == 0:
                g = garo(row, col)
                s = sero(row, col)
                visit(row, col, g, s)
                cur_area = g*s

                if max_area < cur_area:
                    max_area = cur_area

    print(f'#{tc} {max_area}')
