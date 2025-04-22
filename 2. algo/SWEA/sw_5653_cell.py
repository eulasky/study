from pprint import pprint

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 시작 리스트
def find_start_cell():
    for i in range(N+K):
        for j in range(M+K):
            if status[i][j] != 0:
                life = status[i][j]-1
                power = status[i][j]
                start_status.append((i, j, 0, status[i][j]))

def cultivation(arr):
    pq = arr
    visited = [(0, 0) * (M+K) for _ in range(N+K)]
    for si, sj in pq:
        visited[si][sj][0] = status[si][sj]
        visited[si][sj][1] = 1

    while pq:
        ci, cj = pq.pop(0)











T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    status = [[0]*(M+K) for _ in range(N+K)]

    for i in range(N):
        status[K//2+i][K//2:K//2+M] = grid[i]

    start_status = []
    find_start_cell()
    cultivation(start_status)
    pprint(status)