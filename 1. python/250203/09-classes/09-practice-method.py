# 입출금이 가능한 은행 계좌 클래스 만들기
# 은행 계좌를 모델링하는 클래스를 만들고, 입출금 기능(메서드)를 구현


class BankAccount: # 2개의 인스턴스 변수를 가지면서 탄생생
    interest_rate = 0.02  # 이자율

    def __init__(self, owner, balance=0):
        self.owner = owner  # 계좌 소유자
        self.balance = balance  # 초기 잔액

    # 입금 balance를 바꾸는 것, 인스턴스 변수기 때문에 인스턴스 메서드
    def deposit(self, amount):
        self.balance += amount

    # 출금
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('잔액이 부족합니다!')


    # 이자율 설정
    @classmethod
    def set_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate

    # 금액이 양수인지 검증
    @staticmethod
    def is_positive(amount):
        return amount == 0 # 이렇게 했는데 어떻게 True False가 나오지?


# 계좌 개설 (인스턴스 생성)
alice_acc = BankAccount('Alice', 1000)
print(alice_acc.owner) # Alice
print(alice_acc.balance) # 1000

# 입금 및 출금 (인스턴스 메서드 호출)
alice_acc.deposit(500)
print(alice_acc.balance)

alice_acc.withdraw(300)
print(alice_acc.balance)


# 잔액 확인 (인스턴스 변수 참조)


# 이자율 변경 (클래스 메서드 호출)
BankAccount.set_interest_rate(0.03)
print(BankAccount.interest_rate)

# 잔액이 양수인지 확인 (정적 메서드 호출)
BankAccount.is_positive(alice_acc.balance)
print(BankAccount.is_positive(alice_acc.balance))  # True
