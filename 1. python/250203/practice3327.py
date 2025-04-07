class Myth:
    type_of_myth = 0
    
    def __init__(self, name):
        self.name = name
        Myth.increase_number()

    @classmethod
    def increase_number(cls):
        cls.type_of_myth += 1

    @staticmethod
    def description():
        return '신화는 한 나라 혹은 한 민족으로부터 전승되어 오는 예로부터 섬기는 신을 둘러싼 이야기를 뜻한다.'



myth1 = Myth('dangun')
myth2 = Myth('greek & rome')

print(myth1.name)
print(myth2.name)
print(f'현재까지 생성된 신화 수 : {Myth.type_of_myth}')
print(Myth.description())

# return 값이 없으면 None이 뜨지 바보야!, 안하려면 print를 없애주거나 하렴렴