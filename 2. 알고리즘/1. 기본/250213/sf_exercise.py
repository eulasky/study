def find_num(i, N, v):  # 찾는 값
    if i == N:
        return 0
    elif arr[i] == v:
        return 1
    else:
        return f(i+1, N, v)    # 받은 리턴 값을 그대로 보내주는 경우