def test(s):
    for i in s:
        if i in '{[(<':
            push(i)
        elif i == '}':
            if STACK[top] != '{':
                return 0
            else:
                pop()
        elif i == ']':
            if STACK[top] != '[':
                return 0
            else:
                pop()
        elif i == ')':
            if STACK[top] != '(':
                return 0
            else:
                pop()
        elif i == '>':
            if STACK[top] != '<':
                return 0
            else:
                pop()
    if top >= 0:
        return 0
    elif top == -1:
        return 1


def push(s):
    global top
    top += 1
    STACK[top] = s

def pop():
    global top
    top -= 1


T = 10

for tc in range(1, T+1):
    N = int(input())
    s = input()
    STACK = [0] * N
    top = -1

    result = test(s)

    print(f'#{tc} {result}')