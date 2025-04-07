N = 4
lst = ['프랑스', '영국', '태국', '미국']

M = 3

# p = [0, 1, 2]
# p = [0, 1, 3]
# ---
# p = [3, 2, 1]

path = [-1] * M
used = [False] * N
def perm(k, mid):
    if k == M:
        print(path)
        # for i in range(M):
        #     print(lst[path[i]], end = " ")
        print(mid)
        return

    for i in range(N):
        if not used[i]:
            used[i] = True
            path[k] = i
            perm(k+1, mid+[lst[i]])
            used[i] = False

perm(0, [])
