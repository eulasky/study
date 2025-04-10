def sub(k, s):
    global cnt
    if s > K:
        return
    if s == K:
        cnt += 1
        return
    if k == N:
        return

    sub(k+1, s)
    sub(k+1, s+arr[k])

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    sub(0, 0)

    print(f'#{tc} {cnt}')