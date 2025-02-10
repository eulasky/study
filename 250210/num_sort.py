T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    for i in range(N-1):
        min_idx = i
        for j in range(i, N):
            if numbers[min_idx] > numbers[j]:
                numbers[min_idx], numbers[j] = numbers[j], numbers[min_idx]

    print(f'#{test_case} {" ".join(map(str, numbers))}')