def dfs(sr, sc, move):
    global max_move, min_room
    visited = [[0] * N for _ in range(N)]
    stack = []
    stack.append((sr, sc, move))
    visited[sr][sc] = 1

    while stack:
        cr, cc, move = stack.pop()

        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = cr + di, cc + dj
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and room[nr][nc] == room[cr][cc] + 1:
                stack.append((nr, nc, move + 1))
                visited[nr][nc] = 1

    return move


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]

    max_move = 0
    min_room = N * N
    for row in range(N):
        for col in range(N):
            moves = dfs(row, col, 1)
            if max_move < moves:
                max_move = moves
                min_room = room[row][col]
            elif max_move == moves:
                min_room = min(min_room, room[row][col])


    print(f'#{tc} {min_room} {max_move}')
