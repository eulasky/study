def push(s):
    global top
    top += 1
    STACK[top] = s

def pop():
    global top
    top -= 1

def password(s):
    global top
    for i in s:
        if top == -1 or STACK[top] != i:
            push(i)
        else:
            pop()

    password = ''
    for j in range(top+1):
        password += STACK[j]

    return password

T = 10
for tc in range(1, T+1):
    N, s = input().split()
    N = int(N)
    STACK = [0] * N
    top = -1

    result = password(s)

    print(f'#{tc} {result}')