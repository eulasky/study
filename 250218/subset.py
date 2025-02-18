def f(i, N, s, t, rs):        # i는 인덱스, N은 배열 크기, i-1까지 결정한 원소의 합, t는 찾는 값
    global cnt
    cnt += 1
    if s == t:             # 뒤에 return 생략
        print(bit, s)
    elif s > t:             # 찾는 합보다 커지면 중지
        return
    elif i == N:
        return
    elif s + rs < t:        # 남은 원소를 다 더해도 찾을 수 없으면
        return
    else:
        bit[i] = 1        # bit[i]를 1로 결정
        f(i+1, N, s+A[i], t, rs-A[i])   # bit[i+1]을 결정하러 이동
        bit[i] = 0
        f(i+1, N, s, t, rs-A[i])


A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0] * len(A)
cnt = 0
f(0, len(A), 0, 10, sum(A))
print(cnt)

