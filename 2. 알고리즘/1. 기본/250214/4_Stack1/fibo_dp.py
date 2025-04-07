def fibo2(n) :
    f = [0] * (n + 1)   # 테이블이 한 번만 만들어져 있으면, 가져다 쓰면 됨
    f[0] = 0
    f[1] = 1
    for i in range(2, n + 1) :
        f[i] = f[i-1] + f[i-2]

    return f[n]

print(fibo2(10))


