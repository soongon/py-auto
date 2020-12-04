# kakao_key = '41ebdd23985a5d4723db5cd1527312ed'

import requests
import pandas as pd

headers = {
    'Authorization': 'KakaoAK 41ebdd23985a5d4723db5cd1527312ed'
}

params = {
    'query': '2.5단계',
    'size': 50,
    'page': 2
}

res = requests.get('https://dapi.kakao.com/v2/search/web', headers=headers, params=params)

result = res.json()

doc_list = result.get('documents')

articles = []
for doc in doc_list:
    articles.append([
        doc.get('title').replace('<b>', '').replace('</b>', ''),
        doc.get('contents').replace('<b>', '').replace('</b>', ''),
        doc.get('datetime'),
        doc.get('url')
    ])

df = pd.DataFrame(articles)
df.to_csv('kakao_api_news.csv')

print('job completed..')
