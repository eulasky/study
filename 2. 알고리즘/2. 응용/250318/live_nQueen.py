# 4*4 N-Queen 문제
# - (y, x) 좌표에 queen을 놓은 적이 있다.
#   - visited 기록 방법
#       - 1. 이차원 배열
#       - 2. 일차원 배열로 효율적으로 하는 방법

# level: N개의 행에 모두 놓았다. (N개의 행에 모두 놓았다면, 성공.)
# branch: N개의 열

def check(row, col):
    # 1. 같은 열에 놓은 적이 있는가
    for i in range(row):
        if visited[i][col]:
            return False

    # 2. 왼쪽 대각선 (\)
    i, j = row-1, col-1
    while i >= 0 and j >= 0:
        if visited[i][j]:
            return False
        i -= 1
        j -= 1

    # 3. 오른쪽 대각선 (/)
    i, j = row-1, col+1
    while i >= 0 and j < N:
        if visited[i][j]:
            return False
        i -= 1
        j += 1

    # 다 검사했는데 False를 리턴하지 않았다면,
    return True

def dfs(row):
    global answer
    if row == N:
        answer += 1
        return

    # 후보군: N개의 열
    for col in range(N):
        ## 모든 케이스를 보는 것
        ## -> 모든 케이스를 적어 놓고, 고민을 해 보는 것
        # visited[row][col] = 1
        # dfs(row+1)
        # visited[row][col] = 0

        # 가지치기: 유망하지 않은 케이스는 확인하지 않겠다!
        if check(row, col):
            visited[row][col] = 1
            dfs(row+1)
            visited[row][col] = 0


N = 8
visited = [[0] * N for _ in range(N)]
answer = 0  # 가능한 정답 수

dfs(0)
print(answer)


