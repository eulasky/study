def to_dec(s, bit):
    value = 0
    for c in s:
        value = (value*bit) + int(c)
    return value

s = '0000000111100000011000000111100110000110000111100111100111111001100111'
for i in range(0, len(s), 7):
    sub_s = s[i : i+7]
    print(to_dec(sub_s, 2), end = ' ')