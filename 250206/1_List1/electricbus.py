def check()
    if # 간격이 k를 넘어가면:
        return 0

    cnt = 0
    last_stop = 0
    for i in stop을 순회:
        curS = STOP[i]
        if stop - last_stop > K:
            i-1 에서 충전하자:
            cnt += 1
            last_stop = STOP[i-1]



T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    STOP = [0] + list(map(int, input().split())) + [N]

