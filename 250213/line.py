P = int(input())

for tc in range(1, P+1):
    height = list(map(int, input().split()))
    K = height[0]

    cnt = 0
    for i in range(2, 21):
        for j in range(1, i):
            if height[j] >= height[i]:
                for i in range(i, j, -1):
                    height[i], height[i-1] = height[i-1], height[i]
                    cnt += 1

    print(f'{K} {cnt}')