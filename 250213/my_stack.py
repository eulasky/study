# 간단한 스택
top = -1
stack = [0] * 10

# push 1
top += 1
stack[top] = 1

# push 2
top += 1
stack[top] = 2

# push 3
top += 1
stack[top] = 3

# pop
top -= 1
print(stack[top+1])   # 3





