class Dog:
    sound = '멍멍'

class Cat:
    sound = '야옹'


class Pet(Dog, Cat):
    @classmethod
    def __str__(cls):
        return f'애완동물은 {cls.sound} 소리를 냅니다.'

class Pet(Cat, Dog):
    @classmethod
    def __str__(cls):
        return f'애완동물은 {cls.sound} 소리를 냅니다.'
    
Pet1 = Pet()
print(Pet1)