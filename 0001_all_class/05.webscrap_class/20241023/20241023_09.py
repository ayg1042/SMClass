from selenium import webdriver
from selenium.webdriver.common.by import By as by
from selenium.webdriver.common.keys import Keys as keys
import time
import requests, random
from bs4 import BeautifulSoup

url = 'https://flight.naver.com'

if __name__ == '__main__':
  wep = webdriver.Chrome()
  wep.maximize_window() # 창 최대화 (전체화면)
  wep.get(url)
  time.sleep(2)

  # 출발
  elem = wep.find_element(by.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[1]')
  elem.click()
  time.sleep(1)
  
  # 출발지 입력
  elem = wep.find_element(by.XPATH, '//*[@id="__next"]/div/main/div[8]/div[1]/div/input')
  elem.send_keys('김포')
  time.sleep(1)

  # 출발지 선택
  elem = wep.find_element(by.XPATH, '//*[@id="__next"]/div/main/div[8]/div[2]/section/ul/li[2]/a/b')
  elem.click()
  time.sleep(1)

  # 도착지
  elem = wep.find_element(by.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[2]')
  elem.click()
  time.sleep(1)

  # 도착지 입력
  elem = wep.find_element(by.XPATH, '//*[@id="__next"]/div/main/div[8]/div[1]/div/input')
  elem.send_keys('제주')
  time.sleep(1)

  # 도착지 선택
  elem = wep.find_element(by.XPATH, '//*[@id="__next"]/div/main/div[8]/div[2]/section/ul/li/a/b')
  elem.click()
  time.sleep(1)

  # 출발 날짜
  elem = wep.find_element(by.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[2]/button[1]')
  elem.click()
  time.sleep(1)

  # 날짜 선택
  elem = wep.find_element(by.XPATH, '//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[2]/td[4]/button')
  elem.click()
  time.sleep(1)

  # 도착 날짜
  elem = wep.find_element(by.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[2]/button[2]')
  elem.click()
  time.sleep(1)

  # 날짜 선택
  elem = wep.find_element(by.XPATH, '//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div[4]/table/tbody/tr[1]/td[7]/button')
  elem.click()
  time.sleep(1)

  # 인원 선택 창
  elem = wep.find_element(by.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[3]/button')
  elem.click()
  time.sleep(1)

  # 인원 선택 2명
  elem = wep.find_element(by.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[4]/div/div/div[1]/div[1]/button[2]')
  elem.click()
  time.sleep(1)

  # 항공권 검색
  elem = wep.find_element(by.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/button[1]')
  elem.click()
  elem.click()

  # 페이지 전환 대기
  time.sleep(10)


  time.sleep(30)
