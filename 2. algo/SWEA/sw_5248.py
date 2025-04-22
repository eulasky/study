def find_set(x):
    if x == parents[x]:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]




T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    parents = [i for i in range(N+1)]