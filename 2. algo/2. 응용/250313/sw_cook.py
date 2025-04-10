def comb(k, start):
    global result
    if k == N//2:
        p2 = list(set(order) - set(p1))
        cur_result = abs(diff(p1)-diff(p2))
        if result > cur_result:
            result = cur_result
        return
    for i in range(start, N):
        p1[k] = i
        comb(k+1, i+1)

def diff(arr):
    total = 0
    for i in arr:
        for j in arr:
            if i == j:
                continue
            total += ingredient[i][j]
    return total


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ingredient = [list(map(int, input().split())) for _ in range(N)]
    order = [i for i in range(N)]
    p1 = [-1] * (N//2)
    result = 20000

    comb(0, 0)
    print(f'#{tc} {result}')