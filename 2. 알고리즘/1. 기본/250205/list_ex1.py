T = int(input())

for tc in range(1, T+1):
    N = int(input())
    list_N = list(map(int, input().split()))

    min_num = list_N[0]
    max_num = list_N[0]

    for i in range(1, N):
        if min_num > list_N[i]:
            min_num = list_N[i]
        if max_num < list_N[i]:
            max_num = list_N[i]

    result = max_num - min_num
    print(f'#{tc} {result}')
