def check(row, col):
    for i, j in path:
        slope_y = abs(row-i)
        slope_x = abs(col-j)
        if slope_y == 0 or slope_x == 0 or slope_y == slope_x:
            return False

    return True

def queen(row):
    global answer

    if row == N:
        answer += 1
        return

    for col in range(N):
        if check(row, col):
            path.append((row, col))
            queen(row+1)
            path.pop()

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    path = []
    answer = 0

    queen(0)
    print(f'#{tc} {answer}')