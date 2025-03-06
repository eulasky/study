def dec_bi(value):
    s = ""
    while value > 0:
        value = value * 2
        remain = int(value % 2)
        value = value - remain
        s = s + str(remain)
        if len(s) > 12:
            return 'overflow'
    return s


T= int(input())
for tc in range(1, T+1):
    N = float(input())

    result = dec_bi(N)

    print(f'#{tc} {result}')
