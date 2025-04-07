name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


def create_user(name, age, address):
    user_info = {}
    user_info['name'] = name
    user_info['age'] = age
    user_info['address'] = address
    print(f'{name}님 환영합니다!')
    return user_info


many_user = list(map(create_user, name, age, address))
# print(many_user)
# infos = dict(map(lambda x, y : many_user[name], many_user[age], many_user))

d = {'name':'홍길동', 'age':20}
def change(x):
    # new = {'name':x['name'], 'age':20}
    return {'name':x['name'], 'age':20}

infos = list(map(x:{'name':x['name'], 'age':20}, many_user))

infos = list(map(lambda x : {'name' : x[name], 'age' : x['age']}))


infos = []
for i in many_user:
    info = {}
    info['name'] = i['name']
    info['age'] = i['age']
    infos.append(info)

print(infos)


infos = list(map(lambda x, y :
                 
