N = 3
arr = [10, 21, 22]

result = [-1, -1, -1]

# 기본형
def powerset(k):
    if k == N:
        print(result)
        return

    candidates = [1, 0]
    for i in candidates:
        result[k] = i
        powerset(k+1)


# 합
def powerset(k):
    if k == N:
        sumV = 0
        for i in range(N):
            if result[i]:
                sumV += arr[i]
        return

    candidates = [1, 0]
    for i in candidates:
        result[k] = i
        powerset(k + 1)

    # result[k] = 1
    # powerset(k+1)
    # result[k] = 0
    # powerset(k+1)


# 가지치기(유망한지 아닌지를 본다)
def powerset(k, curS):
    if curS > 10:
        return

    if curS == 10:
        return

    if k == N:
        return

    result[k] = 1
    powerset(k+1, curS+arr[k])
    result[k] = 0
    powerset(k+1, curS)