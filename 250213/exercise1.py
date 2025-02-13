txt = input()

top = -1
stack = [0] * 100

ans = 1     # 짝이 맞다고 가정

for x in txt:
    if x == '(':    # 여는 괄호가 여러개인 경우 x in '({[<'
        top += 1
        stack[top] = x
    elif x == ')':  # 중간에 공백이 들어 있을 수 있음
        if top == -1:
            ans = 0
            break   # for x 중단, 어느 부분에 대한 브레이크인지 써주면 좋다
        else:       # 소괄호만 있으므로 비교 작업 생략
            top -= 1

if top > -1:    # 여는 괄호가 남아 있으면
    ans = 0

print(ans)