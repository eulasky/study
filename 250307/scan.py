def hex_to_dec(i):
    arr[i] = arr[i].replace('0', '0000')
    arr[i] = arr[i].replace('1', '0001')
    arr[i] = arr[i].replace('2', '0010')
    arr[i] = arr[i].replace('3', '0011')
    arr[i] = arr[i].replace('4', '0100')
    arr[i] = arr[i].replace('5', '0101')
    arr[i] = arr[i].replace('6', '0110')
    arr[i] = arr[i].replace('7', '0111')
    arr[i] = arr[i].replace('8', '1000')
    arr[i] = arr[i].replace('9', '1001')
    arr[i] = arr[i].replace('A', '1010')
    arr[i] = arr[i].replace('B', '1011')
    arr[i] = arr[i].replace('C', '1100')
    arr[i] = arr[i].replace('D', '1101')
    arr[i] = arr[i].replace('E', '1110')
    arr[i] = arr[i].replace('F', '1111')


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    password = [input() for _ in range(N)]

    for i in password:
        hex_to_dec(i)


