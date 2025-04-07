dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
name = list(input())
total = 0

for char in name:
    for chars in dial:
        time = 0
        if char in chars:
            time = dial.index(chars) + 3
        total += time

print(total)