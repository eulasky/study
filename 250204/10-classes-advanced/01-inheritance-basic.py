class Animal:
    def eat(self):
        print('먹는 중')


class Dog(Animal): # Dog가 Animal 클래스를 인자로 받음 : 상속의 기본 표현
    def bark(self):
        print('멍멍')


my_dog = Dog()

my_dog.bark()  #
my_dog.eat()

# 부모 클래스(Animal) 메서드 사용 가능
