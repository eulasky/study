def pre_order(s):
    pre_o.append(s)
    if lt.get(s) is not None:
        pre_order(lt[s])
    if rt.get(s) is not None:
        pre_order(rt[s])

def in_order(s):
    if lt.get(s) is not None:
        in_order(lt[s])
    in_o.append(s)
    if rt.get(s) is not None:
        in_order(rt[s])

def post_order(s):
    if lt.get(s) is not None:
        post_order(lt[s])
    if rt.get(s) is not None:
        post_order(rt[s])
    post_o.append(s)

N = int(input())
lt = {}
rt = {}
pre_o = []
in_o = []
post_o = []

for _ in range(N):
    root, L, R = input().split()

    if lt.get(root) is None and L != '.':
        lt[root] = L
    if rt.get(root) is None and R != '.':
        rt[root] = R

pre_order('A')
in_order('A')
post_order('A')

print(''.join(pre_o))
print(''.join(in_o))
print(''.join(post_o))
