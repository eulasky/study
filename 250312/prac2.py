def recur(k):
    if k == N:
        print(path)
        sumV = 0
        for i in range(N-1):
            s = path[i]
            e = path[i+1]
            value = arr[s][e]
            sumV += value
        # 마지막 구간에서 사무실로 돌아가는 소모량
        sumV = arr[path][-1][0]

        result = min(result, sumV)
        return

    for i in range(N):
        if not used[i]:
            used[i] = True
            path.append(i)
            recur(k+1)
            path.pop()
            used[i] = False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    path = []
    used = [False] * N
    result = 100*N*N
    path.append(0)
    used[0] = True
    recur(0)
    print(f'#{tc} {result}')


def recur(k, mid):
    global result
    if k == N:
        result = min(result, mid + arr[path[-1]][0])
        return

    if mid > result:
        return

    for i in range(N):
        if not used[i]:
            used[i] = True
            path.append(i)
            recur(k + 1, mid + arr[path[-2]][i])
            path.pop()
            used[i] = False


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 100 * N
    path = [0]
    used = [False] * N
    used[0] = True
    recur(1, 0)
    print(f'#{tc} {result}')