def dfs(sr, sc, k, s):
    stack = []
    stack.append((sr, sc, k, s))

    while stack:
        cr, cc, k, s = stack.pop()
        s += str(pan[cr][cc])
        if k == 7:
            nums.append(s)

        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ni, nj = cr+di, cc+dj
            if 0 <= ni < 4 and 0 <= nj < 4 and k < 7:
                stack.append((ni, nj, k+1, s))



T = int(input())
for tc in range(1, T+1):
    pan = [list(map(int, input().split())) for _ in range(4)]
    nums = []

    for row in range(4):
        for col in range(4):
           dfs(row, col, 1, '')

    result = len(list(set(nums)))

    print(f'#{tc} {result}')
