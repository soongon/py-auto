import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36'
}
res = requests.get('https://www.genie.co.kr/chart/top200', headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

song_trs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

song_list = []
for tr in song_trs:
    song_list.append([
        tr.select_one('td:nth-child(2)').text[0:3].strip(),
        tr.select_one('td:nth-child(5) > a:nth-child(1)').text.strip(),
        tr.select_one('td:nth-child(5) > a:nth-child(2)').text,
        tr.select_one('td:nth-child(5) > a.albumtitle').text,
        'https:' + tr.select_one('td:nth-child(3) img')['src']
    ])

# list of list 를 CSV 혹은 엑셀파일로 저장..
df = pd.DataFrame(song_list)
df.columns = ['순위', '제목', '가수', '앨범명', '이미지 URL']
df.to_csv('scraping_ginie.csv')
df.to_excel('scraping_ginie.xlsx')
print('job completed..')
