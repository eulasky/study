def pre_order(root_idx):
    if root_idx <= N:
        print(TREE[root_idx])
        pre_order(root_idx*2)
        pre_order(root_idx*2 + 1)

def in_order(root_idx):
    if root_idx <= N:
        in_order(root_idx*2)
        print(TREE[root_idx])
        in_order(root_idx*2 + 1)

N = 10
TREE = [0] * (N+1)
for i in range(10):
    TREE[i+1] = chr(ord('A') + i)

pre_order(1)