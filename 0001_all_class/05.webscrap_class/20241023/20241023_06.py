from selenium import webdriver
from selenium.webdriver.common.by import By as by
from selenium.webdriver.common.keys import Keys as keys
import time
import requests, random
from bs4 import BeautifulSoup



url = 'https://www.naver.com'
# 브라우저 열기
browser = webdriver.Chrome()
# 네이버 페이지 이동
browser.get(url)
# 로그인버튼 선택
elem = browser.find_element(by.CLASS_NAME, 'MyView-module__link_login___HpHMW')
# 로그인버튼 클릭
elem.click()
time.sleep(random.randint(2, 5))

# 자바스크립트 호출방법
id = 'ayg1044'
pw = '0'
input_js = f'document.getElementById("id").value="{id}"; document.getElementById("pw").value="{pw}";'
browser.execute_script(input_js)
time.sleep(random.randint(2, 5))
elem = browser.find_element(by.CLASS_NAME, 'btn_login')

# # id값을 입력
# elem = browser.find_element(by.ID, 'id')
# elem.send_keys('ayg1044')
# time.sleep(random.randint(2, 5))
# # pw값 입력
# elem = browser.find_element(by.ID, 'pw')
# elem.send_keys('ayg1044')
# time.sleep(random.randint(2, 5))

elem = browser.find_element(by.CLASS_NAME, 'btn_login')
elem.click()

time.sleep(30)