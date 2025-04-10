N = int(input())
popularity = [0] + list(map(int, input().split()))
areas = [[] for _ in range(N+1)]

for i in range(1, N+1):
    M, *area = map(int, input().split())

    for j in range(M):
        areas[i].append(area[j])

print(areas)
