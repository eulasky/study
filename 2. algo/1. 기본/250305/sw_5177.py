def enq(value):
    global last
    last += 1
    TREE[last] = value

    c = last
    p = c // 2
    while c >= 1 and TREE[c] < TREE[p]:
        TREE[p], TREE[c] = TREE[c], TREE[p]
        c = p               # 순서가 중요
        p = p // 2          # 바뀌면 안됨

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    TREE = [0] * (N+1)
    last = 1

    for i in range(N):
        enq(i)

    print(f'#{tc} {TREE[1]}')
