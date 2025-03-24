def solution(X, Y):
    xl = list(map(int, str(X)))
    yl = list(map(int, str(Y)))

    x_cnt = [0] * 10
    y_cnt = [0] * 10

    for i in xl:
        x_cnt[i] += 1
    for j in yl:
        y_cnt[j] += 1

    result = []
    for k in range(10):
        if x_cnt[k] > 0 and y_cnt[k] > 0:
            k_cnt = min(x_cnt[k], y_cnt[k])
            for _ in range(k_cnt):
                result.append(k)

    result.sort(reverse=True)
    if len(result) == 0:
        answer = "-1"
    elif sum(result) == 0:
        answer = "0"
    else:
        answer = ''.join(map(str, result))

    return answer
