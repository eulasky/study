def decto(value):
    # 149 => '149'
    # 149 => 149//10 => 14, 9
    # 14  => 14//10  => 1, 4
    # 1   => 1//10   => 0, 1
    result = ""
    while value:
        remain = value % 10
        value = value // 10
        print(value, remain)
        result = str(remain) + result

def decto(value, bit):
    # 149 => '149'
    # 149 => 149//10 => 14, 9
    # 14  => 14//10  => 1, 4
    # 1   => 1//10   => 0, 1
    result = ""
    while value:
        remain = value % bit
        value = value // bit
        if remain < 10:
            result = str(remain) + result
        else:
            mapp = {10:'A', 12:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
            result = mapp[remain] + result

            result = chr(ord('A') + (remain-10)) + result



def todec(s):
    # 149 => ((1*10) + 4) * 10) + 9
    value = 0

    for c in s:
        value = (value*10) + int(c)

    return value


def todec(s, bit):
    # 149 => ((1*10) + 4) * 10) + 9
    value = 0

    for c in s:
        value = (value * bit) + int(c)

    return value

def todec(s, bit):
    value = 0

    for c in s:
        if c.isdigit():
            value = (value * bit) + int(c)
        else:
            mapp = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
            value = (value * bit) + mapp[c]

            value = (value * bit) + ord(c)-ord('A') + 10

    return value

value = '149'
todec(value, 2)


