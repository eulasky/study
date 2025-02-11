# 8X8
'''
4
CBBCBAAB
CCCBABCB
CAAAACAB
BACCCCAC
AABCBBAC
ACAACABC
BCCBAABC
ABBBCCAA
'''
# 문자열 s를 입력 받아 회문이면 True
# 아니면 False를 return
def isPalin(s):
    # if s == s[::-1]:
    #     return True
    # return False

    for i in range(N//2):
        if s[i] != s[N-1-i]:
            return False
    return True




N = int(input())
arr = [input() for _ in range(8)]

cnt = 0
for row in range(8):
    # 한 줄에 대해서
    for st in range(8-N+1):
        if isPalin(arr[row][st:st+N]):
            print(arr[row][st:st+N])
            cnt += 1
print(cnt)

# arr2 = list(zip(*arr))  # *arr -> arr의 껍데기 []를 벗긴것과 같음
# a = [1, 2, 3]
# b = [11, 12, 13]
# c = [21, 22, 23]
# arr3 = list(zip(a, b, c))
# print(arr3)

for col in range(8):
    for st in range(8-N+1):
        s = ''
        for row in range(st, st+N):
            s += arr[row][col]
        if isPalin(s):
            cnt += 1
            print(s)
print(cnt)