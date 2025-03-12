def battery(k, mid):
    global result

    if mid > result:
        return

    if k == N:
        if mid < result:
            result = min(result, mid+golf[path[-1]][0])
            return

    for i in range(1, N):

        if used[i] == 1:
            continue

        used[i] = 1
        path.append(i)
        battery(k+1, mid+golf[path[-2]][i])
        path.pop()
        used[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    golf = [list(map(int, input().split())) for _ in range(N)]
    path = [0]  # 지나온 구역을 저장
    used = [0] * (N + 1)  # 지나온 구역 방문 체크
    used[0] = 1
    result = 1001

    battery(1, 0)
    print(f'#{tc} {result}')