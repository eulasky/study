# 아래 클래스를 수정하시오.
class UserInfo:
    def __init__(self):
        self.user_data = {}

    def get_user_info(self):
        self.name = input('이름을 입력하세요: ')
        self.age = input('나이를 입력하세요: ')
        if self.name != '':
            self.user_data['이름'] = self.name
        try:
            int(self.age)
            self.user_data['나이'] = self.age
        except ValueError:
            print('나이는 숫자로 입력해야 합니다.')
        
    def display_user_info(self):
        if len(self.user_data) == 2:
            print('사용자 정보:')
            for data in self.user_data:
                print(f'{data}: {self.user_data[data]}')
        else:
            print('사용자 정보가 입력되지 않았습니다.')
        
    
user = UserInfo()
user.get_user_info()
user.display_user_info()
