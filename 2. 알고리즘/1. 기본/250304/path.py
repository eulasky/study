def solve(curY, curX, pathL, isCut):
    global result

    visited[curY][curX] = True

    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        newX = curX+dx
        newY = curY+dy
        if 0 <= newX < N and 0 <= newY < N and not visited[newY][newX]:
            if ARR[newY][newX] < ARR[curY][curX]:
                solve(newY, newX, pathL+1, isCut)
            elif not isCut and ARR[newY][newX]-K < ARR[curY][curX]
                temp = ARR[newY][newX]
                ARR[newY][newX] = ARR[curY][curX]-1
                solve(newY, newX, pathL+1, True)
                ARR[newY][newX] = temp

        if result < pathL:
            result = pathL

        visited[curY][curX] = False

TC = int(input())
for tc in range(1, TC+1):
    N, K = map(int, input().split())
    ARR = [list(map(int, input().split())) for _ in range(N)]

    maxV = 0
    for i in range(N):
        maxV = max(maxV, max(ARR[i]))

    result = 0

    visited = [[False] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            if ARR[row][col] == maxV:
                solve(row, col, 1, False)

    print(f'{tc} {result}')



