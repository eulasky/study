# 단일 상속
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email


class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        # super()를 통해 Person의 __init__ 메서드 호출
        super().__init__(name, age, number, email) # 중복되는 4줄을 1줄로
        Person.__init__(name, age, number, email) # 동일하게 실행이 될까 O! 
        self.student_id = student_id
        # 단일 상속에서는 가능
        # 하지만 부모 클래스의 이름이 바뀐다면? 그런 상황에서는 super()를 쓰는게 좋음


# super를 사용하지 않았을 때
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email


class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        self.name = name
        self.age = age
        self.number = number
        self.email = email
        self.student_id = student_id
