def ant_move(move, i, j):
    global cnt
    if move == N:
        if i == 0 and j == 0:
            cnt += 1
        return

    ant_move(move+1, i+1, j+1)
    ant_move(move+1, i-1, j-1)


N = int(input())
cnt = 0
ant_move(0, 0, 0)


print(cnt)