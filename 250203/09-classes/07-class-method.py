class Person:
    population = 0

    def __init__(self, name):
        self.name = name
        Person.increase_population() # 인자로 Person이 들어가는 것
    
    @classmethod
    def increase_population(cls):
        cls.population += 1


person1 = Person('Alice')
person2 = Person('Bob')
print(Person.population)  # 2, population은 클래스 변수

Person.increase_population() 
print(Person.population) # 3