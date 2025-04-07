# 아래 클래스를 수정하시오.
class Animal:
    num_of_animal = 0


class Dog(Animal):
    def __init__(self):
        Animal.num_of_animal += 1
    
    def bark(self):
        return '멍멍!'
    

class Cat(Animal):
    def __init__(self, str1):
        Animal.num_of_animal += 1
        self.str1 = str1
    
    def meow(self):
        print(self.str1)


class Pet(Dog, Cat):
    @classmethod
    def access_num_of_animal(cls):
        return f'동물의 수는 {cls.num_of_animal}마리 입니다.'


cat1 = Cat("야옹")
cat1.meow()