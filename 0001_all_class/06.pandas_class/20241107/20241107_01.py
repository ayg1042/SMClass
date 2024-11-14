import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from bs4 import BeautifulSoup
import random
from selenium.webdriver.chrome.options import Options
import pyautogui
import csv

def sreach():
  url = 'https://search.daum.net/search?w=tot&q=2023%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR'
  wep = webdriver.Chrome()
  wep.maximize_window()
  wep.get(url)
  time.sleep(2)

  for i in range(3):
    soup = BeautifulSoup(wep.page_source, 'lxml')
    with open(f'C:/workspace/20241106/daum_movie_{i + 1}.html', 'w', encoding='utf-8') as f:
      f.write(soup.prettify())
    time.sleep(3)
    elem = wep.find_element(By.XPATH, f'//*[@id="morColl"]/div/c-container/div[2]/c-carousel/div/ul/li[{i+3}]/a')
    elem.click()
    time.sleep(3)


for i in range(3):
  title_list = []
  person_list = []
  mdate_list = []
  with open(f'C:/workspace/20241106/daum_movie_{i+1}.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'lxml')

  # print(f'{page + 1}. 페이지')
  data_list = soup.select('#mor_history_id_0 > div > div.flipsnap_view > div > div:nth-child(1) > c-flicking-item > c-layout > div > c-list-doc > ul > li')
  for data in data_list:
    title = data.select_one('c-doc > div > div.item-bundle-mid > div.item-title > c-title > strong > a').text.strip()
    person = data.select_one('c-doc > div > div.item-bundle-mid > div.item-contents > c-contents-desc > p > a').text.strip()
    start = person.find(' ')
    end = person.find('만')
    person = int(person[start:end].strip().replace(',',''))
    mdate = data.select_one('c-doc > div > div.item-bundle-mid > div.item-contents > c-contents-desc-sub > span').text.strip()
    title_list.append(title)
    person_list.append(person)
    mdate_list.append(mdate)
  mbdata = {
    '제목': title_list,
    '관객수': person_list,
    '날짜': mdate_list
  }
  df = pd.DataFrame(mbdata)
  df.to_csv(f'영화_{i+1}.csv', encoding='utf-8')

mb_data1 = pd.read_csv('영화_1.csv', encoding='utf-8')
mb_data2 = pd.read_csv('영화_2.csv', encoding='utf-8')
mb_data3 = pd.read_csv('영화_3.csv', encoding='utf-8')
df = pd.concat([mb_data1.iloc[:, 1:], mb_data3.iloc[:, 1:], mb_data3.iloc[:, 1:]])
df.set_index('제목', inplace=True)
df['관객수'].max()
df['관객수'].min()
df['관객수'].mean()
df['관객수'].nlargest(5)
df['관객수'].nsmallest(5)