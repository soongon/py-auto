import requests
from bs4 import BeautifulSoup
import pandas as pd


def init_header():
    return {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36'
    }


def get_data_from_li(li_list):
    product_list = []
    for li in li_list:
        title = li.select_one('a > dl > dd > div.name').text.strip()
        price = li.select_one('a > dl > dd > div.price-area > div > div.price > em > strong') \
            .text.strip().replace(',', '')
        delivery = ''
        try:
            delivery = li.select_one('a > dl > dd > div.price-area > div > div.delivery > span') \
                .text.strip().replace('\n', '')
        except:
            delivery = '배송 데이터 없음'
        img_url = 'https:' + li.select_one('a > dl > dt > img')['src']
        product_list.append([title, price, delivery, img_url])

    return product_list


def save_to_with_pandas(list_of_list, file_title):
    df = pd.DataFrame(list_of_list)
    df.columns = ['상품명', '가격', '배송정보', '이미지 URL']
    df.to_csv(file_title + '.csv')
    df.to_excel(file_title + '.xlsx')


def main():

    total_list = []
    for i in range(1, 100):
        res = requests.get('https://www.coupang.com/np/campaigns/82/components/194176?page=' + str(i), headers=init_header())
        soup = BeautifulSoup(res.text, 'html.parser')
        product_lis = soup.select('#productList > li')
        product_list = get_data_from_li(product_lis)
        if not product_list:
            break
        total_list.extend(product_list)
        print(i, '페이지 스크래핑 완료')

    save_to_with_pandas(total_list, 'scraping_coupang')

    print('job completed..')


if __name__ == '__main__':
    main()
