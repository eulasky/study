def shelf(k, sum):
    global answer

    if sum >= B:
        if sum - B < answer:
            answer = sum - B
        return
    if k == N:
        return

    shelf(k + 1, sum)
    shelf(k + 1, sum + heights[k])


T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    answer = int(21e8)

    shelf(0, 0)

    print(f'#{tc} {answer}')