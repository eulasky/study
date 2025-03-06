def hex_to_bi(value):
    if value.isdigit():
        value = int(value)
    else:
        mapp = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
        value = mapp[value]

    result = [0, 0, 0, 0]
    for i in range(3, -1, -1):
        remain = value % 2
        value = value//2
        result[i] = remain

    return ''.join(list(map(str, result)))


T = int(input())
for tc in range(1, T+1):
    N, s = input().split()

    result = ''
    for x in s:
        result += hex_to_bi(x)

    print(f'#{tc} {result}')

