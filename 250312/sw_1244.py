T = int(input())
for tc in range(1, T+1):
    num, change = map(int, input().split())
    cards = list(num)

    for i in range(0, change):
        max_idx = i
        for j in range(i+1, len(cards)):
            if cards[max_idx] < cards[j]:
                max_idx = j
            cards[i]
