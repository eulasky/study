T = int(input())

for tc in range(1, T+1):
    a, b = input().split()
    n = len(a)
    m = len(b)

    cnt = 0
    i = j = 0
    while i < n:
        if a[i] == b[j]:
            i += 1
            j += 1
            if j == m:
                cnt += 1
                j = 0
        else:
            i = i - j + 1
            j = 0

    total = len(a) - cnt * len(b) + cnt

    print(f'#{tc} {total}')





