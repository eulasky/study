def cost(i, N, s):
    global min_v

    if min_v < s:     # 중간 합계가 최소 합보다 크면
        return

    if i == N:
        if min_v > s:
            min_v = s

    for j in range(i, N):
        p[i], p[j] = p[j], p[i]     # 자리교환
        cost(i+1, N, s+arr[i][p[i]])   # i+1 자리 결정
        p[i], p[j] = p[j], p[i]     # 원상복구


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    p = [i for i in range(N)]       # p[i] : i행에서 고른 열 번호
    min_v = 10000
    cost(0, N, 0)

    print(f'#{tc} {min_v}')