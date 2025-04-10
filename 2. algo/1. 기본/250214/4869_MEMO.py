def paper(n):
    global memo
    if n >= 3 and memo[n] == 0:
        memo[n] = paper(n-1) + paper(n-2)*2
    return memo[n]


T = int(input())

for tc in range(1, T+1):
    N = int(input()) // 10
    memo = [0] * (N + 2)
    memo[1] = 1
    memo[2] = 3



    print(paper(N))