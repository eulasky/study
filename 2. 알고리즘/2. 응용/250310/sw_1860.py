def ganeung(bbang):
    ba = 0
    for j in range(11112):
        if j > 0 and j % M == 0:
            ba += K
        if bbang[j] > 0:
            ba -= 1
            if ba < 0:
                return 'Impossible'

    return 'Possible'


T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    customer = list(map(int, input().split()))

    bbang = [0] * 11112

    for i in customer:
        bbang[i] += 1

    print(f'#{tc} {ganeung(bbang)}')



