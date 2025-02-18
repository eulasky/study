# 시작위치를 입력 받아서 3을 찾으면 1을, 아니면 0을 return
def dfs(stR, stC):
    STACK = []
    visited = [[False]*N for _ in range(N)]

    STACK.append((stR, stC))
    visited[stR][stC] = True
    while STACK:
        curR, curC = STACK.pop()
        # if arr[curR][curC] == 3:
        #     return 1

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            newR = curR + dr
            newC = curC + dc
            if 0 <= newR < N and 0 <= newC < N and not visited[newR][newC]:
                if arr[newR][newC] == 0:
                    STACK.append((newR, newC))
                    visited[newR][newC] = True
                elif arr[newR][newC] == 3:
                    return 1
    return 0



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().strip())) for _ in range(N)]

    for row in range(N):
        if arr[row].count(2):
            col = arr[row].index(2)
            break

    # for row in range(N):
    #     for col in range(N):
    #         if arr[row][col] == 2:
    #             break
    #     break                         # break 두 번 해야함

    print(f'#{tc} {dfs(row, col)}')