T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    stone = list(map(int, input().split()))
    for _ in range(M):
        i, j = map(int, input().split())
        idx = i - 1

        for long in range(1, j+1):
            if idx - long >= 0 and idx + long < N:
                if stone[idx-long] == 0 and stone[idx+long] == 0:
                    stone[idx - long] = 1
                    stone[idx + long] = 1
                elif stone[idx - long] == 1 and stone[idx + long] == 1:
                    stone[idx - long] = 0
                    stone[idx + long] = 0
    print(f'#{tc} {" ".join(map(str, stone))}')



