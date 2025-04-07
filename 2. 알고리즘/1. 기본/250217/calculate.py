T = 10
for tc in range(1, T+1):
    N = int(input())
    cal = input()
    STACK = [0] * (N+1)
    top = -1
    icp = {'+': 1}
    isp = {'+': 1}

    s = ''
    for x in cal:
        if x != '+':
            s += x
        elif x == '+':
            if top == -1 or isp[STACK[top]] < icp[x]:
                top += 1
                STACK[top] = x
            elif isp[STACK[top]] >= icp[x]:
                while top > -1 and isp[STACK[top]] >= icp[x]:
                    s += STACK[top]
                    top -= 1
                top += 1
                STACK[top] = x
    s += STACK[top]


    STACK = [0] * (N+1)
    top = -1
    for i in s:
        if i != '+':
            top += 1
            STACK[top] = int(i)
        else:
            op2 = STACK[top]
            top -= 1
            op1 = STACK[top]
            top -= 1
            if i == '+':
                top += 1
                STACK[top] = op1 + op2
        print(STACK)

    print(f'#{tc} {STACK[top]}')





