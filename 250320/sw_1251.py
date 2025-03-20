def find_set(x):
    if x == parents[x]:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    ref_x = find_set(x)
    ref_y = find_set(y)

    if ref_x == ref_y:
        return

    if ref_x < ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y

T = int(input())
for C in range(1, T+1):
    N = int(input())
    islands_x = list(map(int, input().split()))
    islands_y = list(map(int, input().split()))
    E = float(input())

    islands = list(zip(islands_x, islands_y))
    costs = []


    for i in range(N):
        for j in range(i+1, N):
            cost = E * (abs(islands[i][0]-islands[j][0])**2 + abs(islands[i][1]-islands[j][1])**2)
            costs.append((i, j, cost))

    costs.sort(key=lambda x: x[2])
    parents = [i for i in range(N)]

    cnt = 0
    result = 0

    for island1, island2, cost in costs:
        if find_set(island1) != find_set(island2):
            union(island1, island2)
            cnt += 1
            result += cost

            if cnt == N-1:
                break

    result = int(result + 0.5)

    print(f'#{C} {result}')




