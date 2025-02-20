def virus(s):
    visited = [0] * (N+1)
    STACK = []
    STACK.append(s)
    visited[s] = 1
    cnt = 0
    while STACK:
        t = STACK.pop()
        for i in network[t]:
            if visited[i] == 0:
                STACK.append(i)
                visited[i] = 1
                cnt += 1
    return cnt


N = int(input())
E = int(input())
network = [[] for _ in range(N+1)]


for _ in range(E):
    v1, v2 = map(int, input().split())
    network[v1].append(v2)
    network[v2].append(v1)

print(virus(1))