from selenium import webdriver
from selenium.webdriver.common.by import By as by
from selenium.webdriver.common.keys import Keys as keys
import requests
from bs4 import BeautifulSoup
import time

browser = webdriver.Chrome()
browser.get('https://naver.com')


# html 위치 찾기
# elem = browser.find_element(by.CLASS_NAME, 'MyView-module__link_login___HpHMW') # 로그인 버튼 

# elem = browser.find_element(by.ID, 'query') # 검색창
# elem.send_keys('네이버 영화') # 글자 입력
# elem.send_keys(keys.ENTER) # 엔터키 입력
# elem.click()

# browser.switch_to.window(browser.window_handles[1]) # 새창 이동

# elem.click() # 클릭
# browser.back() # 뒤로가기
# browser.forward() # 앞으로 가기
# browser.refresh() # 새로고침

elem = browser.find_element(by.NAME, 'pw')


time.sleep(20)