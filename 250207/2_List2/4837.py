T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    cnt_K = 0
    for i in range(1<<12):
        set_cnt = []
        sets = []
        for j in range(12):
            if i & (1<<j):
                set_cnt.append(A[j])

        if len(set_cnt) == N:
            sum = 0
            for num in set_cnt:
                sum += num
            if sum == K:
                cnt_K += 1

    print(f'#{test_case} {cnt_K}')