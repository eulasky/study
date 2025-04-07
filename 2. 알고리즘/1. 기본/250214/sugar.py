N = int(input())

a = N//3
b = N//5

min_cnt = N
for i in range(a+1):
    cnt = i
    for j in range(b+1):
        if i*3 + j*5 == N:
            cnt += j
            if min_cnt > cnt:
                min_cnt = cnt

if min_cnt == N:
    print(-1)

else:
    print(min_cnt)


