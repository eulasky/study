def bitodec(s):
    return int(s, 2)

s = '0000000111100000011000000111100110000110000111100111100111111001100111'
for i in range(0, len(s), 7):
    sb = s[i:i+7]
    num = bitodec(sb)
    print(num, end = " ")

    