

def recur(cnt):
    global cost

    if cnt == N-1:
        new_path = [0] + path + [0]
        total = 0
        for i in range(N):
            total += area[new_path[i]][new_path[i+1]]

        if cost > total:
            cost = total

        return

    for num in range(1, N):
        if used[num] == 0:
            path.append(num)
            used[num] = 1
            recur(cnt+1)
            path.pop()
            used[num] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]

    cost = 10000

    path = []
    used = [0] * N

    recur(0)

    print(f'#{tc} {cost}')

