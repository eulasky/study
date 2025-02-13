P = int(input())

for tc in range(1, P+1):
    height = list(map(int, input().split()))
    K = height[0]

    cnt = 0
    for i in range(2, 21):
        for j in range(1, i):
            if height[j] >= height[i]:
                cnt += i - j
                break

    print(f'{K} {cnt}')