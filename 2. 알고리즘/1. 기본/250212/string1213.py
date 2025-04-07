def BF(t, p):
    cnt = 0
    for i in range(len(t)-len(p)+1):
        for j in range(len(p)):
            if t[i+j] != p[j]:
                break
        else:
            cnt += 1
    return cnt

T = 10

for _ in range(1, T+1):
    tc = int(input())
    p = input()
    t = input()

    print(f'#{tc} {BF(t,p)}')