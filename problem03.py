############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
# Python 제공 메서드 count 사용 시 감점

def find_most_populated(animal_map):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    if animal_map == {}: # 아무것도 없을 때 None 반환
        return None
    
    else: # 값이 있을 때, 함수 실행
        max_animal_num = 0
        for animal in animal_map:
            if animal_map[animal] > max_animal_num:
                max_animal = animal # 수가 현재까지의 가장 큰 애니멀 수보다 클때
    
    return max_animal


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하거나 수정하지 마세요.
# 모든 책임은 삭제 혹은 수정한 본인에게 있습니다.
############## 테스트 코드 삭제 금지 #################
print(find_most_populated({"lion": 5, "tiger": 3, "elephant": 10}))  # 예시: "elephant"
print(find_most_populated({}))                                       # None
print(find_most_populated({"wolf": 4, "wolfdog": 4, "hyena": 4}))     # "wolf"
#####################################################
