from selenium import webdriver
import time

# 브라우저 띄우기
driver = webdriver.Chrome('./chromedriver')

# 쿠팡 사이트로 이동
driver.get('https://login.coupang.com/login/login.pang')

time.sleep(5)

driver.close()

# 로그인 링크를 클릭
# driver.find_element_by_css_selector('#login > a').click()

# 실습 -> 멜론 사이트 이동 -> 멜론차트 클릭 -> 월간 클릭 (클릭 전에 약간씩 time.sleep(2) 정도 해줘야함)
