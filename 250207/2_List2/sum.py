import sys
sys.stdin = open("input.txt", "r")


T = 10

for test_case in range(1, T+1):
    test = int(input())
    arr = []
    for _ in range(100):
        hundred = list(map(int, input().split()))
        arr.append(hundred)



    max_sum = 0
    for row in range(100):
        row_sum = 0
        for col in range(100):
            row_sum += arr[row][col]
        if max_sum < row_sum:
            max_sum = row_sum

    for col in range(100):
        col_sum = 0
        for row in range(100):
            col_sum += arr[row][col]
        if max_sum < col_sum:
            max_sum = col_sum

    dia_sum = 0
    for row in range(100):
        dia_sum += arr[row][row]
    if max_sum < dia_sum:
        max_sum = dia_sum

    reverse = 0
    for row in range(100):
        reverse += arr[row][100-1-row]
    if max_sum < reverse:
        max_sum = reverse

    print(f'#{test} {max_sum}')