def enq(value):
    global last
    last += 1
    TREE[last] = value

    c = last
    p = c // 2
    while c >= 1 and TREE[c] > TREE[p]:
        TREE[p], TREE[c] = TREE[c], TREE[p]
        c = p               # 순서가 중요
        p = p // 2          # 바뀌면 안됨

def deq(value):
    global last
    result = TREE[1]
    TREE[1] = TREE[last]
    last -= 1

    p = 1
    c = p*2
    while c <= last:                 # c는 left를 유지하도록
        if c+1 <= last and TREE[c] < TREE[c+1]:
            c = c+1

        if TREE[p] < TREE[c]:
            TREE[p], TREE[c] = TREE[c], TREE[p]
            p = c
            c = p*2
        else:
            break

    return result



TREE = [0, 20, 15, 19, 4, 13, 11] + [0]*100
last = 6
print(TREE)
enq(23)
print(TREE)
enq(21)
print(TREE)
enq(1)
print(TREE)
