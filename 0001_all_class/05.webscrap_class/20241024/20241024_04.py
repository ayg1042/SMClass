from selenium import webdriver
from selenium.webdriver.common.by import By as by
from selenium.webdriver.common.keys import Keys as keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests, random
from bs4 import BeautifulSoup
import pyautogui as pygui


url = 'https://www.yanolja.com/search/%EA%B0%95%EB%A6%89%20%ED%98%B8%ED%85%94?pageKey=1729747969396'
wep = webdriver.Chrome()
wep.maximize_window()
wep.get(url)

pygui.moveTo(960, 540)
time.sleep(2)
pygui.moveTo(50, 100)
time.sleep(2)
pygui.moveTo(50, 700)
time.sleep(2)
pygui.moveTo(1500, 300)
time.sleep(2)
pygui.moveTo(1500, 800)
time.sleep(2)
pygui.moveTo(960, 540)
time.sleep(2)
pre_height = wep.execute_script('return document.body.scrollHeight')
while True:
  pygui.scroll(-pre_height)
  time.sleep(2)
  curr_height = wep.execute_script('return document.body.scrollHeight')
  if pre_height == curr_height:
    break
  pre_height = curr_height
print('스크롤 내리기 완료!!')

# 마우스를 옮겨 클릭!!
pygui.moveTo(900, 900)
pygui.click()




input('엔터키 입력')
