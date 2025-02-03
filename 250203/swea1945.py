T = int(input())

for i in range(T):
    N = int(input())
    exponent = [0, 0, 0, 0, 0]
    while N != 1:
        if N % 2 == 0:
            exponent[0] += 1
            N = N / 2
        elif N % 3 == 0:
            exponent[1] += 1
            N = N / 3
        elif N % 5 == 0:
            exponent[2] += 1
            N = N / 5
        elif N % 7 == 0:
            exponent[3] += 1
            N = N / 7
        else:
            exponent[4] += 1
            N = N / 11
    
    print(f'#{i+1} {" ".join(map(str, exponent))}')