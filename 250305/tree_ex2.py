# 완전 이진 트리의 전위 순회
def pre_order(n, N):
    if n <= N:              # 실존하는 정점이면,
        print(tree[n])
        pre_order(n*2, N)
        pre_order(n*2+1, N)

N = 9       # 완전 이진 트리 정점 수
tree = [0, 33, 31, 27, 21, 22, 18, 24, 14, 19]

pre_order(1)