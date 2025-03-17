def binary_search(target):
    left = 0
    right = len(A) - 1
    dir = 0

    while left <= right:
        mid = (left+right) // 2

        if A[mid] == target:
            return 1

        # 왼쪽에 정답이 있다.
        if target < A[mid]:
            right = mid - 1
            if dir == -1:
                return 0
            dir = -1

        else:
            left = mid + 1
            if dir == 1:
                return 0
            dir = 1

    return 0

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))

    cnt = 0
    for i in B:
        cnt += binary_search(i)

    print(f'#{tc} {cnt}')