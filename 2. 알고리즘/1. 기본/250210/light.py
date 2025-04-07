T = int(input())
for tc in range(1, T+1):
    N = int(input())
    start = list(map(int, input().split()))
    goal = list(map(int, input().split()))

    cnt = 0
    for i in range(N):
        if start[i] != goal[i]:
            for j in range(i, N):
                start[j] = (start[j]+1)%2
            cnt += 1

    print(f'#{tc} {cnt}')