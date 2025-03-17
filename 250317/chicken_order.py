def subset(k):
    global min_chicken

    for i in range(1 << len(chickens)):
        arr = []
        find_min = [[] for _ in range(len(homes))]
        for j in range(len(chickens)):
            if i & (1 << j):
                arr.append(j)
        if len(arr) == M:
            for i in range(len(homes)):
                for j in arr:
                    find_min[i].append(length[i][j])
            sum = 0
            for i in range(len(homes)):
                sum += min(find_min[i])
            if min_chicken > sum:
                min_chicken = sum



N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
chickens = []
homes = []
min_chicken = N*N*2*N


for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            homes.append((i, j))
        if city[i][j] == 2:
            chickens.append((i, j))

length = [[] for _ in range(len(homes))]
i = 0
for c1, r1 in homes:
    for c2, r2 in chickens:
        length[i].append((abs(r1-r2)+abs(c1-c2)))
    i += 1

subset(0)
print(min_chicken)

