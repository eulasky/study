def dfs(row, col):
    if visited[row][col]:
        return visited[row][col]

    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        newR = row + dr
        newC = col + dc

        if 0 <= newR < N and 0 <= newC < N and arr[row][col] + 1 = arr[newR][newC]:
            visited[row][col] = dfs(newR, newC) + 1
            return visited[row][col]

    return 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split)) for _ in range(N)]

    visited = [[0]*N for _ in range(N)]

    result_cnt = 0
    result_value = 0
    for row in range(N):
        for col in range(N):
            t = dfs(row, col)
            if result_cnt == t:
                result_value = min(result_value, arr[row][col])
            elif result_cnt < t:
                result_cnt = t
                result_value = arr[row][col]

    print(f'#{tc} {result_value} {result_cnt}')