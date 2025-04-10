def push(item, size):
    global top
    top += 1
    if top == size:
        print('overflow!')      # 이런 형식은 디버깅의 목적
    else:
        stack[top] = item

size = 10
stack = [0] * size
top = -1

push(10, size)
top += 1        # 보통은 이것과
stack[top] = 20 # 이것으로도 충분

def pop():
    if len(s) == 0:
        # underflow
        return  # underflow에 해당하는 return 값을 주는게 맞긴 함
    else:
        return s.pop()

def pop():
    global top
    if top == -1:
        print('underflow')
        return 0
    else:
        top -= 1
        return stack[top+1] # top을 내렸기 때문에 +1 해줌

print(pop())

if top > -1:    # pop()
    top -= 1
    print(stack[top+1])