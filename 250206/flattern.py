import sys
sys.stdin = open("input.txt", "r")

T = 10

for test_case in range(1, T+1):
    N = int(input())
    dump = list(map(int, input().split()))
    count = [0] * 100

    max_height = dump[0]
    min_height = dump[0]
    for height in dump:
        count[height - 1] += 1
        if max_height < height:
            max_height = height
        if min_height > height:
            min_height = height

    max_idx = max_height - 1
    min_idx = min_height - 1

    while N != 0:
        if count[max_idx] != 0:
            count[max_idx] -= 1
            count[max_idx - 1] += 1
        else:
            max_idx -= 1
            count[max_idx] -= 1
            count[max_idx - 1] += 1

        if count[min_idx] != 0:
            count[min_idx] -= 1
            count[min_idx + 1] += 1
        else:
            min_idx += 1
            count[min_idx] -= 1
            count[min_idx + 1] += 1

        N -= 1

    result = max_idx - min_idx

    print(f'#{test_case} {result}')









