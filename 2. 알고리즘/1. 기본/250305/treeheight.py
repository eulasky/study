T = int(input())
for tc in range(1, T+1):
    N = int(input())
    trees = list(map(int, input().split()))
    max_t = max(trees)
    diff = []

    for x in trees:
        diff.append(max_t - x)

    total = sum(diff)

    if max(diff) == 1:
        result = sum(diff) * 2 - 1
    elif max(diff) == 2:
        a = diff.count(1)
        b = diff.count(2)
        c = min(a, b)
        if a > b:
            result = b*c + a*2-1
        elif a < b:
            result = a*c + b*2
        else:
            result = c * 2

    else:
        if total % 3 == 0:
            result = (total//3) * 2
        elif total % 3 == 1:
            result = (total//3) * 2 + 1
        elif total % 3 == 2:
            result = (total//3) * 2 + 2

    print(f'#{tc} {result}')