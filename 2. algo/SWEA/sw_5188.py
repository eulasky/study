def move(ci, cj, total):
    global min_sum

    if total > min_sum:
        return
    if ci == N-1 and cj == N-1:
        if total < min_sum:
            min_sum = total

    if ci < N-1:
        move(ci+1, cj, total+pan[ci+1][cj])
    if cj < N-1:
        move(ci, cj+1, total+pan[ci][cj+1])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    pan = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 1690

    move(0, 0, pan[0][0])

    print(f'#{tc} {min_sum}')