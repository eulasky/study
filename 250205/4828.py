T = int(input())

for i in range(1, T+1):
    N = int(input())
    list_N = list(map(int, input().split()))

    min_num = list_N[0]
    max_num = list_N[0]

    for number1 in list_N:
        if number1 >= max_num:
            max_num = number1

    for number2 in list_N:
        if number2 <= min_num:
            min_num = number2

    result = max_num - min_num
    print(f'#{i} {result}')