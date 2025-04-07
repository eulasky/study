'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
def pre_order(root):
    print(root)
    if TREE[root]:
        pre_order(TREE[root][0])
    if len(TREE[root]) == 2:
        pre_order(TREE[root][1])

def in_order(root):
    if TREE[root]:
        in_order(TREE[root][0])
    print(root)
    if len(TREE[root]) == 2:
        in_order(TREE[root][1])

def last_order(root):
    if TREE[root]:
        last_order(TREE[root][0])
    if len(TREE[root]) == 2:
        last_order(TREE[root][1])
    print(root)


N = 13
s = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
TREE = [[] for _ in range(N+1)]
lst = list(map(int, s.split()))
for i in range(0, len(lst), 2):
    p = lst[i]
    c = lst[i+1]
    TREE[p].append(c)

print(TREE)
pre_order(1)

N = 13
s = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
TREE = [[0, 0] for _ in range(N+1)]
lst = list(map(int, s.split()))
for i in range(0, len(lst), 2):
    p = lst[i]
    c = lst[i+1]
    if TREE[i][0]:
        TREE[i][1] = c
    else:
        TREE[i][0] = c

def pre_order(root):
    print(root)
    if TREE[root][0]:
        pre_order(TREE[root][0])
    if TREE[root][1]:
        pre_order(TREE[root][1])

def pre_order(T):
    if T:
        print(T)
        pre_order(TREE[T][0])
        pre_order(TREE[T][1])

def post_order(T):
    if T:
        post_order(TREE[T][0])
        post_order(TREE[T][1])
        print(T)
