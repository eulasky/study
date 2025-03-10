def candy(arr):
    cnt = 0
    for i in range(2, 0, -1):
        if arr[i] <= arr[i-1]:
            diff = arr[i-1] - arr[i]
            arr[i-1] = arr[i] - 1
            cnt += diff + 1
            if arr[i-1] <= 0:
                return -1
    return cnt

T = int(input())
for tc in range(1, T+1):
    candies = list(map(int, input().split()))
    result = candy(candies)

    print(f'#{tc} {result}')


