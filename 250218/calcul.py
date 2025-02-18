def cals(s):
    result = ''
    STACK = []
    pr = {'+' : 1, '*' : 2}
    for x in s:
        if x not in '+*':
            result += x
        else:
            if not STACK or pr[STACK[-1]] < pr[x]:
                STACK.append(x)
            else:
                while STACK and pr[STACK[-1]] >= pr[x]:
                    result += STACK.pop()
                STACK.append(x)

        while STACK:
            result += STACK.pop()

    STACK = []
    for c in result:
        if c.isdigit():
            STACK.append(int(c))
        else:
            op2 = STACK.pop()
            op1 = STACK.pop()
            if c == '*':
                STACK.appned(op1 * op2)
            elif c == '+':
                STACK.append(op1 + op2)

    return STACK(-1)




T = 10
for tc in range(1, T+1):
    N = int(input())
    s = input().strip()

    print(f'#{tc} {cals(s)}')