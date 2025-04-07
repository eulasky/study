import sys
sys.setrecursionlimit(1000000)

def find_set(x):
    if x == parents[x]:
        return x

    parents[x] = find_set(parents[x])

    return parents[x]

def union_set(x, y):
    ref_x = find_set(x)
    ref_y = find_set(y)

    if ref_x == ref_y:
        return

    elif ref_x < ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y

n, m = map(int, input().split())

parents = [i for i in range(n+1)]

for _ in range(m):
    q, a, b = map(int, input().split())

    if q == 0:
        union_set(a, b)
    elif q == 1:
        if find_set(a) == find_set(b):
            print('YES')
        else:
            print('NO')