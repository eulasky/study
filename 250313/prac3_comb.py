N = 4
lst = ['프랑스', '영국', '태국', '미국']

M = 3

# p = [0, 1, 2]
# p = [0, 1, 3]
# p = [0, 2, 3]
# p = [1, 2, 3]

p = [-1] * M

def comb(k, start, mid):
    if k == M:
        print(p)
        # for i in range(M):
        #     print(lst[p[i]], end=" ")
        print(mid)
        return

    for i in range(start, N):
        p[k] = i
        comb(k+1, i+1, mid+[lst[i]])

comb(0, 0, [])