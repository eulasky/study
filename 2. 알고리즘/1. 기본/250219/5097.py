T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    for _ in range(M):
        a = numbers.pop(0)
        numbers.append(a)

    print(f'#{tc} {numbers[0]}')