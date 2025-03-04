def preorder_traverse(T):   # 전위 순회
    if T:                   # T is not None
        visit(T)            # print(T.item)
        preorder_traverse(T.left)
        preorder_traverse(T.right)

def preorder_traverse(T):   # 전위 순회
    if T:                   # T is not None
        visit(T)            # print(T.item)
        preorder_traverse(T.left)
        preorder_traverse(T.right)

def postorder_traverse(T):   # 후위 순회
    if T:                   # T is not None
        preorder_traverse(T.left)
        preorder_traverse(T.right)
        visit(T)            # print(T.item)

# 5번 노드의 조상 찾기
c = 5
while a[c] != 0:
    c = a[c]
    anc.append(c)
root = c