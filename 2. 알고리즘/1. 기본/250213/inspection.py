def is_pair(s):
    STACK = []
    for c in s:
        if c == '(':
            STACK.append(c)
        elif c == ')':
            if len(STACK) > 0: # 데이터 있을 때만
                # not STACK:
                    # return False
                temp = STACK.pop(-1)
                if temp != '(':
                    return False
            else:
                return False

    if STACK:
        return False
    return True


s = '()()((()))'
print(is_pair(s))