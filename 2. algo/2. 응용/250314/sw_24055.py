T = int(input())
for tc in range(1, T+1):
    n = int(input())
    numbers = list(map(int, input().split()))

    max_cnt = 0
    for i in range(n-1):
        max_v = numbers[i]
        cnt = 0
        for j in range(i+1, n):
            if max_v < numbers[j]:
                max_v = numbers[j]
                cnt += 1
        if max_cnt < cnt:
            max_cnt = cnt

    print(f'#{tc} {max_cnt}')
