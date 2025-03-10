# 1. BFS로 접근
#   -이동 방향: 상하좌우
#   -무조건 상하좌우로 가능하지 않다.
#       -이동이 불가능한 케이스
#           -[델타 배열 기본] 범위 밖으로 나가면 못감
#           -[방문 기록 기본] 이미 방문한 곳은 안감
#           -[문제 조건]
#               -현재 내 위치에서 뚫려있는 곳으로만 이동 가능
#               -다음 가려는 곳의 터널이 뚫려있는 곳으로만 이동 가능
#               -> 이런 케이스는 델타 배열 순서와 동일하게,
#                       이동 가능 여부를 기록해두면 좋다.
# 2. 방문 기록을 해야 한다 (visited)

from collections import deque

# 리스트에서 제일 앞에 데이터를 꺼내면 리스트의 길이만큼 시간이 발생
# q = [1, 2, 3]
# q.pop(0)      # 0(리스트의 길이)
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 터널들의 종류에 따라, 이동 가능 여부
types = {
    1:[1, 1, 1, 1],
    2:[1, 1, 0, 0],
    3:[0, 0, 1, 1],
    4:[1, 0, 0, 1],
    5:[0, 1, 0, 1],
    6:[0, 1, 1, 0],
    7:[1, 0, 1, 0]
}

def bfs(R, C):
    dq = deque([(R, C)])    # 후보군
    visited[R][C] = 1       # 출발점 초기화

    while dq:
        nowy, nowx = dq.popleft()
        dirs = types[graph[nowy][nowx]]

        for i in range(4):  # 4방향을 확인하면서
            # 출구가 안열려 있는 경우 continue
            new_y = nowy + dy[i]
            new_x = nowx + dx[i]

            # 범위 밖으로 넘어가면 pass
            # 여기선 안될 때 가지마라 할 때가 더 가독성이 높음
            if new_y < 0 or new_y >= N or new_x < 0 or new_x >= M:
                continue

            # 이미 방문했다면 pass
            if visited[new_y][new_x]:
                continue

            # 못가면 pass
            if graph[new_y][new_x] == 0:
                continue

            # 다음 좌표 터널 뚤린 것을 확인
            next_dirs = types[graph[new_y][new_x]]

            # 현재 상좌 -> next_dirs가 하우 안뚫렸으면 못감
            if i % 2 == 0 and next_dirs[i+1] == 0:
                continue

            # 현재 하우 -> next_dirs가 상좌 안뚫렸으면 못감
            if i % 2 == 1 and next_dirs[i-1] == 0:
                continue

            # 시간을 +1 해주면서 기록
            visited[new_y][new_x] = visited[nowy][nowx] + 1
            dq.append((new_y, new_x))




T = int(input())
for tc in range(1, T+1):
    # 5개의 변수가 각각 의미를 가지고 있다.
    # -> 리스트로 안 만드는 게 더 편하다.
    N, M, R, C, L = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    # 특정 좌표까지 몇 시간이 걸렸는 지 기록
    visited = [[0]*M for _ in range(N)]

    bfs(R, C)

    cnt = 0
    for i in range(N):
        for j in range(M):
            if 0 < visited[i][j] <= L:
                cnt += 1

    print(f'{tc} {cnt}')
