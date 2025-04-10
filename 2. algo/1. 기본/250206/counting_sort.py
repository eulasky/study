def counting():
    count = [0] * 10 # count[0], count[1], ... , count[9]
    for number in numbers:
        count[number] += 1

    for i in range(9):
        count[i+1] = count[i] + count[i+1]

    temp = [-1] * N
    for number in numbers:
        # position = count[number] - 1
        # temp[position] = number
        # count[number] -= 1

        count[number] -= 1
        temp[count[number]] = number

    print(temp)






N = 8
numbers = [0, 4, 1, 3, 1, 2, 4, 2]
# => [0, 1, 1, 2, 2, 3, 4, 4]
# => [0, 0, 0, 0, 0, 0, 0, 0]

counting()


N = 4
numbers = [0, 9, 0, 9]

counting()

N = 6
numbers = [2, 2, 2, 2, 2, 2]

counting()

N = 1
numbers = [2]

counting()