import requests
from pprint import pprint

def get_author_info(author_name):
    url = "https://ko.wikipedia.org/w/api.php"
    
    params = {
        'action': 'query',
        'format': 'json',
        'prop': 'extracts|pageimages',
        'titles': author_name,  # 작가 이름
    }

    response = requests.get(url, params=params)
    data = response.json()

    # API 응답을 출력하여 확인하기
    print(data)  # 응답 전체 출력
    
    # 반환된 데이터에서 필요한 정보 추출
    pages = data['query']['pages']
    
    # pages에 내용이 없으면 결과가 없다는 의미
    if not pages:
        return {"error": "작가 정보를 찾을 수 없습니다."}
    
    page_id = next(iter(pages))  # 첫 번째 페이지 ID
    title = pages[page_id].get('title', '정보 없음')
    extract = pages[page_id].get('extract', '작가 정보가 없습니다.')
    image_url = None

    # 작가 프로필 사진 URL 추출
    if 'thumbnail' in pages[page_id]:
        image_url = pages[page_id]['thumbnail']['source']
    
    return {
        'title': title,
        'extract': extract,
        'image_url': image_url
    }

author_name = "헤르만 헤세"  # 예시
author_info = get_author_info(author_name)
pprint(author_info)
