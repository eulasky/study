N, M = map(int, input().split())
select = list(map(int, input().split()))
numbers = [i for i in range(1, N + 1)]

q = []

cnt = 0
for i in select:
    j = 0
    while j < len(numbers) and numbers[j] != i:
        q.append(numbers.pop(0))

    numbers.pop(0)

    if len(numbers) >= len(q):
        cnt += len(q)
        numbers += q

    else:
        cnt += len(numbers) + 1
        numbers += q

    q = []

print(cnt)