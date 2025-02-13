# 0 1 2 3 4 5 6 7
# 0 1 1 2 3 5 8 13

# n의 index의 fibo 값을 return한다
def fibo(n):
    if n < 2:
        return n

    f1 = fibo(n-1)
    f2 = fibo(n-2)
    return f1 + f2

fibo(3)