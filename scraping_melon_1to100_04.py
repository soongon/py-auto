import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36'
}

res = requests.get('https://www.melon.com/chart/index.htm', headers=headers)

soup = BeautifulSoup(res.text, 'html.parser')

song_trs = soup.select('#frm > div > table > tbody > tr')

for i, tr in enumerate(song_trs):
    print(i + 1, ' : ', tr.select_one('td:nth-child(4) > div > div > div:nth-child(1) > span > a').text)
