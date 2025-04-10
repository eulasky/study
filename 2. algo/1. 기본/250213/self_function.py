def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

    cnt = 0
    print(fibo(10), cnt)

def f(i, N):
    if i == N:
        return