# kakao_key = '41ebdd23985a5d4723db5cd1527312ed'

import requests

headers = {
    'Authorization': 'KakaoAK 41ebdd23985a5d4723db5cd1527312ed'
}

params = {
    'query': '2.5단계'
}

res = requests.get('https://dapi.kakao.com/v2/search/web', headers=headers, params=params)

import pprint
pprint.pprint(res.json())
