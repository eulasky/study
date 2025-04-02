def find_num(N):
    s = 0

    for i in range(11):
        for j in range(10):
            s += down_nums[i][j]

            if s >= N:
                remain = down_nums[i][j] - (s-N)
                result_nums.append(j)
                if remain < 0:
                    result_nums.append(0)
                    return

                idx = i
                while remain != 0:
                    idx -= 1
                    for k in range(10):
                        if sum_nums[idx][k] >= remain:
                            s = sum_nums[idx][k]
                            remain -= s
                            result_nums.append(k)
                            break
                return







N = int(input())

down_nums = [[0]*10 for _ in range(11)]
result_nums = []

for i in range(10):
    down_nums[1][i] = 1

for i in range(2, 11):
    for j in range(i-1, 10):
        down_nums[i][j] = down_nums[i-1][j-1] + down_nums[i][j-1]

# down_nums 복사
sum_nums = [down_nums[i][::] for i in range(11)]

# 바로 찾아갈 수 있게 누적값 만들기
for i in range(11):
    for j in range(1, 10):
        sum_nums[i][j] = sum_nums[i][j] + sum_nums[i][j-1]

find_num(N)

result = ''.join(map(str, result_nums)) if result_nums else -1
print(result)






