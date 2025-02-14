def dfs1(st):
    STACK = []
    visited = [False] * (N+1)
    STACK.append(st)

    while STACK:    # 스택에 데이타가 있는 경우, len(STACK) > 0
        v = STACK.pop(-1)
        # STACK에서 pop 해서 사용한다.
        if not visited[v]:
            print(v)
            visited[v] = True
        for w in G[v]:
            if not visited[w]:
                STACK.append(w)

def dfs2(st):

    STACK = []
    visited = [False] * (N+1)

    STACK.append(st)
    visited[st] = True
    while STACK:
        v = STACK.pop(-1)
        print(v)

        for w in G[v]:
            if not visited[w]:
                STACK.append(w)
                visited[w] = True

visited = [False] * (7+1)   # 재귀로 사용할 것이기 때문에
def dfs_r(v):
    print(v)
    visited[v] = True

    for w in G[v]:
        if not visited[w]:
            dfs_r(w)




lst = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
# 인접한 것 짝을 지어 넣어 놓은 것
# 이런 입력이 들어오면 그래프로 표현할 수 있어야 함
# G = [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], ...]
''' 
v node하고 연결된 노드들은?
-> G[v]
-> 이렇게 그래프를 만들어야 한다
'''
N = 7
G = [[] for _ in range(N+1)]
print(G)

for i in range(0, len(lst), 2):
    p1 = lst[i]
    p2 = lst[i+1]
    G[p1].append(p2)    # 방향이 있는 경우에는 방향으로
    G[p2].append(p1)    # 방향이 없는 경우에는 양방향으로 서로를 바라보게
print(G)

# print(G)    # 그래프는 논리적인 자료구조인데, 그걸 2차원 리스트로 만든 것

dfs1(1)
dfs2(1)
dfs_r(1)