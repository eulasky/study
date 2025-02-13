T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if M > N:
        max_sum = 0
        for i in range(M-N+1):
            sum = 0
            for j in range(N):
                sum += a[j] * b[i+j]

            if max_sum < sum:
                max_sum = sum
    else:
        max_sum = 0
        for i in range(N-M+1):
            sum = 0
            for j in range(M):
                sum += b[j] * a[i + j]

            if max_sum < sum:
                max_sum = sum

    print(f'#{tc} {max_sum}')
