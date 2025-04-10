import sys
sys.stdin = open("input2.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    # 행 검사
    result_row = 0
    for row in range(9):
        cnt = 0
        for i in range(1, 10):
            if i in sudoku[row]:
                cnt += 1
        if cnt == 9:
            result_row += 1

    # 열 검사
    result_col = 0
    for col in range(9):
        cnt = 0
        count_list = [0] * 9
        for row in range(9):
            count_list[sudoku[row][col]-1] += 1
        if 0 not in count_list:
            result_col += 1

    # 사각형 검사
    result_square = 0
    for row in range(0, 7, 3):
        for col in range(0, 7, 3):
            cnt = 0
            count_list2 = [0] * 9
            for row2 in range(3):
                for col2 in range(3):
                    count_list2[sudoku[row + row2][col + col2]-1] += 1
            if 0 not in count_list2:
                result_square += 1

    if result_row + result_col + result_square == 27:
        print(f'#{test_case} 1')

    else:
        print(f'#{test_case} 0')



