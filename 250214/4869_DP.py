def paper():
    f[1] = 1
    f[2] = 3
    for i in range(3, 31):
        f[i] = f[i-1] + 2 * f[i-2]


T = int(input())
f = [0] * 31
paper()
for tc in range(1, T+1):
    N = int(input())

    print(f'#{tc} {f[N//10]}')
