T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    weights = list(map(int, input().split()))
    trucks = list(map(int, input().split()))

    weights.sort(reverse=True)
    trucks.sort(reverse=True)
    i = 0
    total = 0
    for t in range(len(trucks)):
        if i < len(weights):
            for w in range(i, len(weights)):
                if trucks[t] >= weights[w]:
                    total += weights[w]
                    i = w+1
                    break

    print(f'#{tc} {total}')
