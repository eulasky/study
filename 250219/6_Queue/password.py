T = 10

for _ in range(1, T+1):
    tc = int(input())
    numbers = list(map(int, input().split()))

    i = 0
    while True:
        number = numbers.pop(0)
        i = (i+1)%6
        number = number - i
        if i == 5:
            i = 0
        if number > 0:
            numbers.append(number)
        else:
            number = 0
            numbers.append(number)
            break
    print(f'#{tc}', *numbers)
