number_of_people = 0

def increase_user():
    global number_of_people
    number_of_people += 1


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


def create_user(name, age, address):
    user_info = {}
    user_info['name'] = name
    user_info['age'] = age
    user_info['address'] = address
    print(f'{name}님 환영합니다!')
    increase_user()
    return user_info


many_user = list(map(create_user, name, age, address))
infos = list(map(lambda x : {'name' : x['name'], 'age' : x['age']}, many_user))


def rental_book(info):
    borrow = info['age']//10
    name = info['name']
    decrease_book(borrow)
    print(f'{name}님이 {borrow}권의 책을 대여하였습니다.')

number_of_book = 100

def decrease_book(borrow):
    global number_of_book
    number_of_book -= borrow
    print(f'남은 책의 수 : {number_of_book}')

list(map(rental_book, infos))