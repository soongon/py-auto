from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')

driver.get('https://www.melon.com/index.htm')
time.sleep(2)

driver.find_element_by_css_selector('#gnb_menu > ul:nth-child(1) > li.nth1 > a').click()
time.sleep(2)

driver.find_element_by_css_selector('#gnb_menu > ul:nth-child(1) > li.nth1.on > div > ul > li:nth-child(4) > a').click()
time.sleep(5)

driver.close()
