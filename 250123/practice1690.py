import requests
from pprint import pprint as print


dummy_data = []

for i in range(1, 11):
    # 무작위 유저 정보 요청 경로
    API_URL = f'https://jsonplaceholder.typicode.com/users/{i}'
    # API 요청
    response = requests.get(API_URL)
    # JSON -> dict 데이터 변환
    parsed_data = response.json()
    info = {
        'company' : parsed_data['company']['name'], 
        'lat' : parsed_data['address']['geo']['lat'],
        'lng' : parsed_data['address']['geo']['lng'],
        'name' : parsed_data['name'],
    }
    if -80 < float(info['lat']) < 80 and -80 < float(info['lng']) < 80:
        dummy_data.append(info)


black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]


def create_user(user_data):
    censored_user_list = {}
    for user in user_data:
        check = censorship(user)
        if check == True:
            censored_user_list[user['company']] = [user['name']]
    
    return censored_user_list


def censorship(user2):
    if user2['company'] in black_list:
        print(f"{user2['company']} 소속의 {user2['name']} 은/는 등록할 수 없습니다.")
        return False
    else:
        print('이상 없습니다.')
        return True

print(create_user(dummy_data))
