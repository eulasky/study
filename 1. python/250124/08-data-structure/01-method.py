print(type('1'))
print(type([1, 2]))
print(help(str))


def add(a, b): # 함수 add
    return a + b

class Calculator:
    def add(self, a, b): # 메서드 add
        return a + b
    
# 함수 호출
add(1, 2) # 독자적으로 호출

# 메서드 호출
a = Calculator() # 어떠한 객체가 호출출
a.add(1, 2)

# 문자열 메서드 예시
print('hello'.capitalize()) # Hello

# 리스트 메서드 예시
numbers = [1, 2, 3]
numbers.append(4)