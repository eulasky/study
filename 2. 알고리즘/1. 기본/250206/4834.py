T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    numbers = map(int, list(input()))
    temp = [0] * 10

    for number in numbers:
        temp[number] += 1

    max_count = -1
    for i in range(len(temp)):
        if temp[i] > max_count:
            max_count = temp[i]
            max_number = i
        elif temp[i] == max_count:
            if max_number < i:
                max_number = i


    print(f'#{test_case} {max_number} {max_count}')




