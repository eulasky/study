def BF(t, p):
    N = len(t)
    M = len(p)

    tp = pp = 0
    while tp < N and pp < M:
        if t[tp] == p[pp]:
            tp += 1
            pp += 1
        else:
            tp = tp-pp+1
            pp = 0
    if pp == M:
        return tp-M
    return -1


t = 'TTTTAACCA'
p = 'TTA'
print(BF(t, p))



def KMP(t, p):
    N = len(t)
    M = len(p)

    lps = [0] * (M+1)  # 패턴 분석
    lps[0] = -1
    j = 0
    for i in range(1, M):
        lps[i] = j
        if p[i] == p[j]:
            j += 1
        else:
            j = 0
    lps[M] = j

    print(lps)

    tp = pp = 0
    while tp < N and pp < M:
        if lps[pp] == -1 or t[tp] == p[pp]:
            tp += 1
            pp += 1
        else:
            pp = lps[pp]
    if pp == M:
        return tp-M
    return -1

t = 'zzzabcabcdabcefsss'
p = 'abcdabcef'
print(KMP(t, p))

p = 'aabc'
print(KMP(t, p))

p = 'ababc'
print(KMP(t, p))


# 보이어-무어

def BM(t, p):
    N = len(t)
    M = len(p)

    jump = [M] * (ord('z') + 1) # count?
    for i in range(M):
        idx = ord(p[i])
        jump[idx] = M-1-i


    # print(jump[ord('r')])
    # print(jump[ord('m')])

    tp = pp = M-1

    while tp < N and 0 <= pp:
        if t[tp] == p[pp]:
            tp -= 1
            pp -= 1
        else:
            idx = ord(t[tp])
            tp += jump[idx]
            pp = M-1

    if pp == -1:
        return tp + 1
    return -1


t = 'a pattern matching algorithm'
p = 'rithm'

print(BM(t, p))

t = 'a pattern matching algorithm'
p = 'a pa'

print(BM(t, p))

t = 'a pattern matching algorithm'
p = ' mat'

print(BM(t, p))

t = 'a pattern matching algorithm'
p = 'aaaa'

print(BM(t, p))