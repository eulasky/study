T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    stone = list(map(int, input().split()))
    for _ in range(M):
        i, j = map(int, input().split())
        color = stone[i-1]
        if i+j-1 <= N:
            for pos in range(i, i+j-1):
                stone[pos] = color
        else:
            for pos in range(i, N):
                stone[pos] = color

    print(f'#{tc} {" ".join(map(str, stone))}')