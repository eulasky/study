class Counter:
    def __init__(self): # 생성자 메서드도 인스턴스 메서드
        # Counter.__init__(self)
        self.count = 0
    
    def increment(self):
        self.count += 1


c = Counter()
print(c.count) # 0
c.increment()
print(c.count) # 1

c2 = Counter()
c.increment()
print(c2.count) # 0 # c2는 increment()를 호출한 적이 없다

print(type(c))
print(type(c2))

