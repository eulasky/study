N = int(input())
papers = [list(map(int, input().split())) for _ in range(N)]
area = [[0] * 1001 for _ in range(1001)]

for i in range(1, N+1):
    r, c, h, w = papers[i-1]

    for row in range(r, r+h):
        area[row][c:c+w] = [i]*w

for j in range(1, N+1):
    c_cnt = 0
    for row in range(1001):
        c_cnt += area[row].count(j)
    print(c_cnt)