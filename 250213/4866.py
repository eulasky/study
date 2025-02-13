T = int(input())

for tc in range(1, T+1):
    s = input()
    STACK = [0] * 50
    top = -1

    ans = 1

    for i in s:
        if i in '({':
            top += 1
            STACK[top] = i
        elif i == ')':
            if top == -1:
                ans = 0
                break
            elif STACK[top] == '{':
                ans = 0
                break
            elif STACK[top] == '(':
                top -= 1
                ans = 1

        elif i == '}':
            if top == -1:
                ans = 0
                break
            elif STACK[top] == '(':
                ans = 0
                break
            elif STACK[top] == '{':
                top -= 1
                ans = 1
    if top > -1:
        ans = 0

    print(f'{tc} {ans}')