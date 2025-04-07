numbers = [i for i in range(1000001)]
for i in range(2, 10**6+1):
    for j in range(2, (10**6)//i+1):
        numbers[i*j] = False

for x in range(2, 1000001):
    if numbers[x]:
        print(numbers[x], end = ' ')
