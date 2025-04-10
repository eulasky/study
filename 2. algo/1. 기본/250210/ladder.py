import sys
sys.stdin = open("input_ladder.txt", "r")

def ladder_start(arr):
    j = 0
    while arr[99][j] != 2:
        j += 1

    col = j
    for row in range(99, -1, -1):
        if 0 <= col-1 and arr[row][col-1] == 1: # 없으면 안됨 경우를 정해주고 거기서 반복
            while 0 <= col-1 and arr[row][col-1] != 0:
                col -= 1
        elif col+1 <= 99 and arr[row][col+1] == 1:
            while col+1 <= 99 and arr[row][col+1] != 0:
                col += 1

    return col

T = 10
for tc in range(T):
    testcase = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    start = ladder_start(ladder)

    print(f'#{testcase} {start}')