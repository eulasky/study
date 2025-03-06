import sys
sys.stdin = open("tree.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    trees = list(map(int, input().split()))
    diff = []
    max_t = max(trees)
    for i in trees:
        diff.append(max_t-i)

    odd_cnt = 0
    even_cnt = 0
    for i in diff:
        if i%2 == 1:
            even_cnt += i//2
            odd_cnt += 1
        elif i != 0 and i%2 == 0:
            even_cnt += i//2

    if odd_cnt > even_cnt:
        day = even_cnt*2 + ((odd_cnt-even_cnt)*2)-1
    elif odd_cnt == even_cnt:
        day = even_cnt*2
    else:
        plus = even_cnt-odd_cnt
        plus2 = (plus//3)*4
        plus3 = 0
        if plus%3 == 1:
            plus3 = 2
        elif plus%3 == 2:
            plus3 = 3
        day = odd_cnt*2 + plus2 + plus3

    print(f'#{tc} {day}')