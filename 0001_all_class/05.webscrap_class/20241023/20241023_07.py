from selenium import webdriver
from selenium.webdriver.common.by import By as by
from selenium.webdriver.common.keys import Keys as keys
import time
import requests, random
from bs4 import BeautifulSoup

url = 'https://www.daum.net'
browser = webdriver.Chrome
browser.get(url)

elem = browser.find_element(by.CLASS_NAME, 'btn_login')
time.sleep(random.randint(2, 5))
elem.click()

id = 'att'
pw = 'att'

input_js = f'document.getElementById("loginId--1").value = "{id}";\
  document.getElementById("password--2").value = "{pw}";'

browser.execute_script(input_js)
# 대기
time.sleep(random.randint(2, 5))
# 클릭

elem = browser.find_element(by.CLASS_NAME, 'btn_g')
elem.click()