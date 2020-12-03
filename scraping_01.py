# 위치 선정.. URL .. https://news.naver.com

# 해당 URL로 요청을 보냄 --> 해당 서버는 요청한 URL 리소스를 응답해줌 --> HTML.. 응답

# HTTP 요청을 보내는 모듈 (HTTP agent, web agent, HTTP client) --> requests (천하통일)

import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.daum.net/')

soup = BeautifulSoup(res.text, 'html.parser')

the_tag = soup.select_one('#cSub > div > ul > li:nth-child(1) > div.item_issue > div > strong > a')

print(the_tag.text)
