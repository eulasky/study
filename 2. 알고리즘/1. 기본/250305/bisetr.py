def insert(value):
    idx = 1
    while TREE[idx]:
        if TREE[idx] < value:
            idx = idx*2 + 1
        else:
            idx = idx*2
    TREE[idx] = value

def find(key):
    idx = 1
    while idx < SIZE and TREE[idx]:
        if TREE[idx] == key:
            return idx
        if TREE[idx] < key:
            idx = idx*2 + 1
        else:
            idx = idx*2
    return -1

N = 8
lst = [9, 4, 12, 3, 6, 15, 13, 17]
TREE = [0] * 100

for data in lst:
    insert(data)
    print(TREE)
