def hex_to_bi(value):
    mapp = {'0':'0000',
            '1':'0001',
            '2':'0010',
            '3':'0011',
            '4':'0100',
            '5':'0101',
            '6':'0110',
            '7':'0111',
            '8':'1000',
            '9':'1001',
            'A':'1010',
            'B':'1011',
            'C':'1100',
            'D':'1101',
            'E':'1110',
            'F':'1111',}
    return mapp[value]

def password(s):
    tr = {'001101':'0',
          '010011':'1',
          '111011':'2',
          '110001':'3',
          '100011':'4',
          '110111':'5',
          '001011':'6',
          '111101':'7',
          '011001':'8',
          '101111':'9',}
    return tr[s]

s = '0269FAC9A0'
bi_s = ''
for x in s:
    bi_s += hex_to_bi(x)

print(bi_s)

for i in range(len(bi_s)-1, -1, -1):
    if bi_s[i] == '1':
        break

pw = []
for j in range(i, -1, -6):
    bi_num = bi_s[j-5:j+1]
    if '1' in bi_num:
        num = password(bi_num)
        pw.append(num)

pw.reverse()
print(*pw)