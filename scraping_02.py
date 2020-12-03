import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.yanolja.com/pension')

soup = BeautifulSoup(res.text, 'html.parser')

the_tag = soup.select_one('#__next > div:nth-child(1) > div.fvxgtis.gqhaWX > main > section:nth-child(3) > div > a:nth-child(1) > div._1_Ism_ > div._20_GPK')

print(the_tag.text)