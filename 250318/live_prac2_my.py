def subset(k, s):
    if s > 10:
        return
    if s == 10:
        print(arr)
        return
    if k == N:
        return

    subset(k+1, s)
    arr.append(powerset[k])
    subset(k+1, s+powerset[k])
    arr.pop()



N = 10
powerset = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr = []

subset(0, 0)