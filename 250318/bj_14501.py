def don(k, s):
    global max_cash

    if k > N:
        max_cash = max(max_cash, s)
        return

    don(k+1, s)
    if k+time[k] <= N:
        don(k+time[k], s+cash[k])

N = int(input())
time = [0]
cash = [0]
max_cash = 0
for _ in range(N):
    t, c = map(int, input().split())
    time += [t]
    cash += [c]

don(1, 0)

print(max_cash)