N, M = map(int, input().split())
cards = list(map(int, input().split()))

max_sum = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            cards_sum = cards[i] + cards[j] + cards[k]
            if cards_sum <= M:
                if max_sum < cards_sum:
                    max_sum = cards_sum

print(max_sum)