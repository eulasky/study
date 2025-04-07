def f(k, mid_sum):
    global max_value, min_value

    if k == N-1:
        if max_value < mid_sum:
            max_value = mid_sum
        if min_value > mid_sum:
            min_value = mid_sum

        return

    if op[0] > 0:
        op[0] -= 1
        f(k+1, mid_sum+numbers[k+1])
        op[0] += 1
    if op[1] > 0:
        op[1] -= 1
        f(k+1, mid_sum-numbers[k+1])
        op[1] += 1
    if op[2] > 0:
        op[2] -= 1
        f(k+1, mid_sum*numbers[k+1])
        op[2] += 1
    if op[3] > 0:
        op[3] -= 1
        f(k+1, int(mid_sum/numbers[k+1]))
        op[3] += 1



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    op = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    max_value = -100000000
    min_value = 100000000

    f(0, numbers[0])

    print(f'#{tc} {max_value-min_value}')
