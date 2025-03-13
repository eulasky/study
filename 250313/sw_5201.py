T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    weight = list(map(int, input().split()))
    capacity = list(map(int, input().split()))

    weight.sort(reverse=True)
    capacity.sort(reverse=True)

    total = 0
    w = c = 0
    while w < len(weight) and c < len(capacity):
        if capacity[c] >= weight[w]:
            total += weight[w]
            w += 1
            c += 1
        else:
            w += 1

    print(f'#{tc} {total}')

