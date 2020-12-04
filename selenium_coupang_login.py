from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 브라우저 띄우기
driver = webdriver.Chrome('./chromedriver')

# 쿠팡 로그인 사이트로 이동
driver.get('https://login.coupang.com/login/login.pang')
time.sleep(2)

# 아이디 인풋박스에 아이디 입력
driver.find_element_by_name('email').send_keys('soongon@gmail.com')
time.sleep(1)
driver.find_element_by_name('password').send_keys('znvkd!#%')
time.sleep(1)
driver.find_element_by_css_selector('body > div.member-wrapper.member-wrapper--flex > div > div > form > div.login__content.login__content--trigger > button')\
    .click()
time.sleep(1)
driver.find_element_by_css_selector('#header > section > div > ul > li.cart.more > a').click()
time.sleep(1)

page_html = driver.page_source

time.sleep(1)

driver.close()

from bs4 import BeautifulSoup

soup = BeautifulSoup(page_html, 'html.parser')

# 로그인 링크를 클릭
# driver.find_element_by_css_selector('#login > a').click()

# 실습 -> 멜론 사이트 이동 -> 멜론차트 클릭 -> 월간 클릭 (클릭 전에 약간씩 time.sleep(2) 정도 해줘야함)
