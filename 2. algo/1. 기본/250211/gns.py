T = int(input())

for _ in range(1, T+1):
    tcl = input().split()
    tc = tcl[0]
    N = int(tcl[1])
    numbers = input().split()
    num_dict = {}

    for i in range(N):
        if num_dict.get(numbers[i]) is None:
            num_dict[numbers[i]] = 1
        else:
            num_dict[numbers[i]] += 1

    print(tc)
    for j in ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']:
        if num_dict.get(j) is not None:
            for k in range(num_dict[j]):
                print(j, end = ' ')