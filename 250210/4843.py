def special(arr, N):
    for i in range(10):
        idx = i
        if i % 2 == 0:
            for j in range(i+1, N):
                if arr[idx] < arr[j]:
                    idx = j
        else:
            for j in range(i+1, N):
                if arr[idx] > arr[j]:
                    idx = j

        arr[idx], arr[i] = arr[i], arr[idx]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    # 1 10 1 9 2 8 3 7 4 6 5
    # 2 89 8 85 11 67 16 60 28 49 39
    # 3 98 3 97 9 88 17 75 18 71 21 69 26 64 30 62 36 60 43 59 46

    special(numbers, N)
    new = numbers[:10]

    print(f'#{tc} {" ".join(map(str, new))}')
