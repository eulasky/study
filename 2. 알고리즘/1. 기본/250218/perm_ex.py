def f(i, N, s):
    global min_v
    if i == N:
        if min_v > s:
            min_v = s
    elif min_v < s:     # 중간 합계가 최소합보다 크면
        return
    else:
        for j in range(i, N):
            p[i], p[j] = p[j], p[i]     # 자리교환
            f(i+1, N, s+arr[i][p[i]])                   # i+1 자리 결정
            p[i], p[j] = p[j], p[i]     # 원상복구


N = int(input())    # 배열의 크기 N x N
arr = [list(map(int, input().split())) for _ in range(N)]

p = [i for i in range(N)]   # P[i] : i행에서 고른 열 번호
min_v = 10000
f(0, N, s)