N = 4
lst = ['프랑스', '영국', '태국', '미국']

# 2^4
p = [-1] * N
def recur(k, mid):
    if k == N:
        # print(p)
        # for i in range(N):
        #     if p[i] == 1:
        #         print(lst[i], end = ' ')
        print(mid)
        return

    # for i in range(2):
    #     p[k] = i
    #     recur(k+1)

    # p[k] = 0
    recur(k+1, mid)
    # p[k] = 1
    recur(k+1, mid+[lst[k]])

recur(0, [])