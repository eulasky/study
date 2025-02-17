stack = [0]*100
top = -1

icp = {'(' : 3, '*' : 2, '/' : 2, '+' : 1, '-' : 1}
isp = {'(' : 0, '*' : 2, '/' : 2, '+' : 1, '-' : 1}

fx = '(6+5*(2-8)/2)'
susik = ''

for x in fx:
    if x not in'(+-*/)':            # 연산자가 아니라면
        susik += x                  # 수식에 넣음
    elif x == ')':                  # 닫는 괄호면
        while stack[top] != '(':    # 여는 괄호가 나올 때까지
            susik += stack[top]     # 수식에 stack[top]을 넣어라
            top -= 1
        top -= 1                    # 여는 괄호를 빼니까
    else:
        if top == -1 or isp[stack[top]] < icp[x]:   # 우선순위 탐색, 밖에 있는게 더 높으면
            top += 1                                # push
            stack[top] = x
        elif isp[stack[top]] >= icp[x]:             # 우선순위 탐색, 밖에 있는게 안이랑 같거나 작으면
            while top > -1 and isp[stack[top]] >= icp[x]:   # 커질때까지 pop
                susik += stack[top]
                top -= 1
            top += 1  # push
            stack[top] = x

# susik += stack[top] << 확인해봐야함
print(susik)