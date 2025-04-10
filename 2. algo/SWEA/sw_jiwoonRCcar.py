def find_start(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'X':
                return i, j


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    area = [list(input()) for _ in range(N)]

    si, sj = find_start(area)  # start 지점 찾기

    Q = int(input())
    result = [0] * Q
    ans = 0

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    d = 0
    for i in range(Q):
        C, command = input().split()

        ci = si
        cj = sj
        for i in range(int(C)):
            if command[i] == 'A':
                ni = si + dy[d]
                nj = sj + dx[d]
                if 0 <= ni < N and 0 <= nj < N:
                    ci = ni
                    cj = nj
            elif command[i] == 'R':
                d = (d+1)%4
            elif command[i] == 'L':
                d = (d-1)%4
            else:
                continue

        if area[ci][cj] == 'Y':
            ans = 1

        result.append(ans)

    print(f'#{tc}', ' '.join(result))


