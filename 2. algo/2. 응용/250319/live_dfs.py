import sys
sys.stdin = open("graph.txt", "r")

def dfs(node):
    # 보통 그래프 문제들에서
    # 이곳에는 가지치기가 들어감
    # ex) K개의 노드를 방문했다면 종료
    # ex) N개를 모두 방문했다면 경로 출력
    # if 종료시 해야할 것들 or 가지치기:
    #       return

    print(node, end = " ")

    # visited[1] = 1 -> 밖에 초기화 하는 것과 차이가 뭘지 생각

    # 현재 노드에서 인접한 노드들을 모두 확인하면서, 한 군데로 진행
    for next_node in graph2[node]:
        # 이미 방문했다면 가지마라!
        if visited[next_node]:
            continue

        visited[next_node] = 1
        dfs(next_node)

    # 종료 조건을 따로 주지 않아도, visited 조건 때문에 끝나게 된다


N, M = map(int, input().split())
# 1. 그래프를 저장하기
#   - 비어있는 그래프를 생성한다
#   - 그래프 정보를 입력받아 넣는다

# 항상 N+1 로 해주는 것을 잊지 마라!!!

# 인접 행렬 (N*N의 0배열)
graph1 = [[0]*(N+1) for _ in range(N+1)]

# 인접 행렬 보기 좋게 하기
# for row in graph1:
#     print(*row)

# 인접 리스트 (N*N ([]))
graph2 = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    graph2[s].append(e)     # 유방향일 땐, 이게 끝
    graph2[e].append(s)     # 양방향일 땐, 둘 다 써주어야 함

visited = [0] * (N+1)       # 방문 여부 기록, 재귀이기 때문에 밖에다 만들어 둠
visited[1] = 1
dfs(1)
