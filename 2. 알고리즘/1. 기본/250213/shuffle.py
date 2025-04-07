T = int(input())

for tc in range(1, T+1):
    N = int(input())
    card = input().split()
    new_card = []

    if N % 2 == 1:
        f = card[:N//2+1]
        l = card[N//2+1:]

        for i in range(N//2):
            new_card.append(f[i])
            new_card.append(l[i])

        new_card.append(f[i+1])

    else:
        f = card[:N//2]
        l = card[N//2:]

        for i in range(N//2):
            new_card.append(f[i])
            new_card.append(l[i])

    print(f'#{tc} {" ".join(new_card)}')