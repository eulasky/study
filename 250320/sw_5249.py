def find_set(x):    # 대표자 찾기
    if x == parents[x]:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):    # 합치기
    mas_x = find_set(x)
    mas_y = find_set(y)

    if mas_x == mas_y:
        return

    if mas_x < mas_y:
        parents[mas_y] = mas_x
    else:
        parents[mas_x] = mas_y



T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    tree = []

    for i in range(E):
        n1, n2, w = map(int, input().split())
        tree.append((n1, n2, w))

    tree.sort(key = lambda x: x[2])
    parents = [i for i in range(V+1)]

    cnt = 0
    total = 0
    for info in tree:
        st, end, w = info
        if find_set(st) != find_set(end):
            union(st, end)
            cnt += 1
            total += w

            if cnt == V:
                break

    print(f'#{tc} {total}')

