from collections import deque

def cal(N, M):
    visited = [0] * 1000001
    visited[N] = 1
    q = deque([N])

    while q:
        c = q.popleft()

        if c == M:
            return visited[c]-1

        for oper in [c+1, c-1, c*2, c-10]:
            if oper > 1000000:
                continue
            if visited[oper] != 0:
                continue

            q.append(oper)
            visited[oper] = visited[c]+1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    print(f'#{tc} {cal(N, M)}')