T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    list_N = list(map(int, input().split()))

    min_sum = 0
    for num in list_N:
        min_sum += num

    max_sum = 0

    for i in range(M):
        temp_sum = 0
        temp_arr = list_N[i : i+N-M+1]

        for num in temp_arr:
            temp_sum += num

        if min_sum > temp_sum:
            min_sum = temp_sum

        if max_sum < temp_sum:
            max_sum = temp_sum

    result = max_sum - min_sum

    print(result)