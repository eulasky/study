def move(sr, sc, total):
    global result
    if total > result:
        return
    if sr == N-1 and sc == N-1:
        if result > total:
            result = total
        return

    if sr < N-1:
        move(sr+1, sc, total+pan[sr+1][sc])

    if sc < N-1:
        move(sr, sc+1, total+pan[sr][sc+1])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    pan = [list(map(int, input().split())) for _ in range(N)]
    used = [[0]*N for _ in range(N)]
    result = 1690

    move(0, 0, pan[0][0])
    print(f'#{tc} {result}')