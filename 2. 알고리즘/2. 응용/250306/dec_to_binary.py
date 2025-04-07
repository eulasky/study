target = 74

def dec_to_binary(target):
    binary_number = ""

    while target > 0:
        remain = target % 2     # 1. 2로 나눈 나머지
        binary_number = str(remain) + binary_number
        target = target // 2    # 2로 나눈다.
    print(binary_number)
    return binary_number

def binary_to_dec(binary_str):
    # 1. binary_str 문자열 뒤에서 부터 진행
    # 2. 각 자리에 맞는 수를 곱하면서, 결과에 더한다.
    decimal_number = 0
    pow = 0

    for digit in reversed(binary_str):
        if digit == '1':
            decimal_number += 2 ** pow
        pow += 1
    print(decimal_number)


binary_to_dec(dec_to_binary(target))