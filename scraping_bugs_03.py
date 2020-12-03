import requests
from bs4 import BeautifulSoup

res = requests.get('https://music.bugs.co.kr/chart/track/realtime/total')

soup = BeautifulSoup(res.text, 'html.parser')

the_tag = soup.select_one('#CHARTrealtime > table > tbody > tr:nth-child(1) th > p > a')
print(the_tag.text)

#CHARTrealtime > table > tbody > tr:nth-child(1) > input > input > th > p > a
#CHARTrealtime > table > tbody > tr:nth-child(1) > th > p > a