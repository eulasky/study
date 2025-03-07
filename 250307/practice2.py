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

s = '01D06079861D79F99F'

bi = ''
for i in s:
    bi += hex_to_bi(i)

for j in range(0, len(bi), 7):
    seven = bi[j:j+7]
    print(int(seven, 2), end=' ')

