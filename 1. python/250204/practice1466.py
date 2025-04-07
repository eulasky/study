# 아래 함수를 수정하시오.
def check_number():
    try: 
        num = int(input('숫자를 입력하세요: '))
        if num > 0:
            print('양수입니다.')
        elif num == 0:
            print('0입니다.')
        else:
            print('음수입니다.') # 이렇게 해도 오류가 안나려나? 양수 0 음수만 존재하나
    except ValueError:
        print('잘못된 입력입니다.')


check_number()