def is_babygin(arr):
    for i in range(10):
        if arr[i] >= 3:
            return 1
        if arr[i] >= 1 and arr[i+1] >= 1 and arr[i+2] >= 1:
            return 1
    return 0

T = int(input())
for tc in range(1, T+1):
    numbers = list(map(int, input().split()))
    count_one = [0] * 12
    count_two = [0] * 12

    answer = 0
    for i in range(len(numbers)):
        if i%2 == 0:
            count_one[numbers[i]] += 1
            if is_babygin(count_one):
                answer = 1
                break
        else:
            count_two[numbers[i]] += 1
            if is_babygin(count_two):
                answer = 2
                break

    print(f'#{tc} {answer}')
