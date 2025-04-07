def cal(w1, w2):
    c = card[w1-1] - card[w2-1]
    if c > 0:
        if c==1:
            return w1
        else:
            return w2
    elif c < 0:
        if c==-1:
            return w2
        else:
            return w1
    else:
        return w1

def game(left, right):
    if left == right:
        return left

    m = (left + right)//2
    winner1 = game(left, m)
    winner2 = game(m+1, right)

    return cal(winner1, winner2)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card = list(map(int, input().split()))

    print(f'#{tc} {game(1, N)}')