T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    hex_num = list(input())
    numbers = []
    dec_num = []

    for _ in range(N//4):
        for i in range(4):
            numbers.append(hex_num[i*(N//4):i*(N//4)+(N//4)])

        x = hex_num.pop()
        hex_num = [x] + hex_num

    for x in numbers:
        dec_num.append(int(''.join(x), 16))

    new = list(set(dec_num))
    new.sort(reverse=True)
    print(f'#{tc} {new[K-1]}')