def push(value):
    global top
    if not is_full():
        top += 1
        STACK[top] = value

def is_full():
    return top == SIZE -1

def is_empty():
    if top == -1:
        return True
    else:
        return False

def pop():
    global top

    if not is_empty():
        value = STACK[top]
        top -= 1
        return value

def peek():
    return STACK[top]

SIZE = 20   # 변경하지 않겠다
STACK = [-1] * SIZE
top = -1

push(3)
print(top, STACK)

push(4)
print(top, STACK)

push(10)
print(top, STACK)

print(pop())
print(top, STACK)

a = pop()
print(a)

