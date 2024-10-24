from selenium import webdriver
from selenium.webdriver.common.by import By as by
from selenium.webdriver.common.keys import Keys as keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests, random
from bs4 import BeautifulSoup

url = 'https://www.yanolja.com/'

if __name__ == '__main__':
  wep = webdriver.Chrome()
  wep.maximize_window() # 창 최대화 (전체화면)
  wep.get(url)

  # 메인화면에서 검색 버튼
  elem = wep.find_element(by.XPATH, '//*[@id="__next"]/div/div/header/section/a[2]')
  elem.click()
  time.sleep(3)

  # 날짜 선택 버튼
  elem = wep.find_element(by.XPATH, '//*[@id="__next"]/div/main/div/div[1]/form/div/div[2]/div[1]/button')
  elem.click()
  time.sleep(2)

  # 날짜 선택
  elem = wep.find_element(by.XPATH, '/html/body/div[4]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[3]/td[2]')
  elem.click()
  time.sleep(1)
  elem = wep.find_element(by.XPATH, '/html/body/div[4]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[3]/td[4]')
  elem.click()
  time.sleep(1)
  elem = wep.find_element(by.XPATH, '/html/body/div[4]/div/div/section/section[4]/button')
  elem.click()
  time.sleep(2)

  # 지역, 장소 등 검색
  elem = wep.find_element(by.XPATH, '//*[@id="__next"]/div/main/div/div[1]/form/div/div[1]/div/input')
  elem.click()
  time.sleep(1)
  elem.send_keys('강릉 호텔')
  time.sleep(1)
  elem.send_keys(keys.ENTER)

  # 페이지 이동시 로딩 대기
  # 화면의 호텔검색내용이 뜰때까지 대기, 최대 30초까지 대기
  WebDriverWait(wep, 30).until(lambda x : x.find_element(by.XPATH, '//*[@id="__next"]/div/main/section/div[2]'))

  # 화면을 스크롤해서 내리기 반복
  # excute_script() : 자바스크립트 실행함수
  prev_height = wep.execute_script('return document.body.scrollHeight')

  while True:
    # 스크롤 내림
    wep.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    # 화면 로딩 대기
    time.sleep(1)
    # 페이지가 로딩되면서 길어진 길이를 다시 가져옴
    curr_height = wep.execute_script('return document.body.scrollHeight')
    print('이전 길이 : ', prev_height)
    # 이전 최대 높이와 현제 최대 높이 비교
    if prev_height == curr_height:
      break
    prev_height = curr_height
  
  soup = BeautifulSoup(wep.page_source, 'lxml')
  # 저장하기
  with open('20241024/yanolja.html', 'w', encoding='utf-8') as f:
    f.write(soup.prettify())
  
  # 불러오기
  with open('20241024/yanolja.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'lxml')

  input('엔터')