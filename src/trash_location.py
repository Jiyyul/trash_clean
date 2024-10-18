import requests

# 발급받은 API 키를 입력
API_KEY = 'vXmg7Fad8Jmi0PG4FtI9beEAt7Io8s610h10dDlO5lQnJU5Rq8ltgGBoNDbps1wnrRtGpQZk47JqLhJzBim07A%3D%3D'
# 동작구 가로쓰레기통 API URL
url = 'http://infuser.odcloud.kr/oas/docs?namespace=15038054/v1'

# 요청 파라미터 설정
params = {
    'serviceKey': API_KEY,
    'some_parameter': 'value',  # 필요한 파라미터 추가
}

# API 호출
response = requests.get(url, params=params)

# 응답 확인
if response.status_code == 200:
    data = response.json()  # JSON 데이터로 변환
    #print(data)

    # 데이터가 리스트 형태로 반환된다고 가정
    items = data.get('items', [])  # 'items'는 API 응답의 데이터 리스트 키
    
    # 필요한 값 추출
    도로명 = data.get('도로명(가로)명', {}).get('type', '')
    설치위치 = data.get('설치위치', {}).get('type', '')
    설치지점 = data.get('설치지점', {}).get('type', '')

    print(f"도로명: {도로명}, 설치위치: {설치위치}, 설치지점: {설치지점}")
else:
    print(f'Error: {response.status_code}')
