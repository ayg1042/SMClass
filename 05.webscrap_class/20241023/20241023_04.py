# 다음사이트에서 검색창에 주식정보 입력해서 페이지 이동을 하시오.
from selenium import webdriver
from selenium.webdriver.common.by import By as by
from selenium.webdriver.common.keys import Keys as keys
import time

browser = webdriver.Chrome()
browser.get('https://www.daum.net')

elem = browser.find_element(by.ID, 'q')
elem.click()
elem.send_keys('주식정보')
elem.send_keys(keys.ENTER)

browser.get('https://www.naver.com')
elem = browser.find_element(by.CLASS_NAME, 'search_input')
elem.send_keys('주식정보')
time.sleep(2)
elem.send_keys(keys.ENTER)

time.sleep(10)


# import time, random

# print(random.uniform(1, 3)) # 실수값
# print(random.randint(1, 3))


# # a = [0]*100
# # for i in range(100):
# #   a[i] = i
# # print(a)

# b = [i for i in range(100)]
# print(b)
# for i in b:
#   print(i)
#   time.sleep(random.uniform(0, 2))