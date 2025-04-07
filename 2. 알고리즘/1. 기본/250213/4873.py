def push(s):
    global top
    top += 1
    STACK[top] = s

def pop():
    global top
    top -= 1

def duplicate(s):
    global top
    for x in s:
        if top == -1 or STACK[top] != x:
            push(x)
        else:
            pop()
    if top == -1:
        return 0
    elif top >= 0:
        return top+1






T = int(input())

for tc in range(1, T+1):
    s = list(input())
    STACK = [0] * len(s)
    top = -1

    result = duplicate(s)
    print(f'#{tc} {result}')