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

# 제목, 금액, 평점, 평가수, 찜 정보를 1 ~ 5페이지까지 가져와서
# 평점 4.8이상, 평가수 1000명 이상 상품 출력

# 1.
# 네이버 쇼핑 검색창 입력 enter키 입력
# 네이버 쇼핑 클릭
# 네이버 쇼핑에서 무선 마우스 검색창 입력 enter키 입력

def naver_sreach():
  url = 'https://www.naver.com'
  wep = webdriver.Chrome()
  wep.maximize_window()
  wep.get(url)
  time.sleep(2)

  elem = wep.find_element(By.XPATH, '//*[@id="query"]')
  elem.click()
  time.sleep(2)

  elem.send_keys('네이버 쇼핑')
  time.sleep(1)
  elem.send_keys(Keys.ENTER)
  time.sleep(3)

  elem = wep.find_element(By.XPATH, '//*[@id="main_pack"]/section[1]/div/div/div[1]/div/div[2]/a')
  elem.click()
  time.sleep(3)

  # 다음텝 페이지 전환
  next_page = wep.window_handles[1]
  wep.switch_to.window(window_name=next_page)

  elem = wep.find_element(By.XPATH, '//*[@id="gnb-gnb"]/div[2]/div/div[2]/div/div[2]/form/div[1]/div/input')
  elem.click()
  elem.send_keys('무선 마우스')
  time.sleep(1)
  elem.send_keys(Keys.ENTER)
  time.sleep(3)

  for i in range(5):
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
    # 2번 클릭
    elem = wep.find_element(By.XPATH, f'//*[@id="content"]/div[1]/div[4]/div/a[{i+1}]')
    elem.click()
    time.sleep(3)
    soup = BeautifulSoup(wep.page_source, 'lxml')
    with open(f'20241025/naver_market_{i+1}.html', 'w', encoding='utf-8') as f:
      f.write(soup.prettify())
  

  # url = wep.current_url
  # return url
# 5개 가져오기 함수
# naver_sreach()

title = ['제목', '금액', '평점', '평가수', '찜']

for j in range(5):
  with open(f'20241025/naver_market_{j+1}.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'lxml')

  # print(f'{page + 1}. 페이지')
  data = soup.select('#content > div.style_content__xWg5l > div.basicList_list_basis__uNBZx > div > div')
  print(len(data))
  # print(data[0])
  # print(data[0].select_one('.adProduct_inner__W_nuz'))
  shop_data = []
  for i in data:
    ad = i.select_one('.adProduct_inner__W_nuz')
    if ad != None:
      name = ad.select_one('.adProduct_info_area__dTSZf > .adProduct_title__amInq > a').text.strip().replace('/n', '')
      money = ad.select_one('.adProduct_info_area__dTSZf > .adProduct_price_area__yA7Ad > strong > .price > .price_num__S2p_v > em').text.strip().replace('/n', '')
      point = ad.select_one('.adProduct_info_area__dTSZf > .adProduct_etc_box__UJJ90 > .adProduct_etc___brfw > a > .adProduct_rating__PaMzh')
      if point != None:
        point = float(point.text.strip().replace('/n', ''))
      else:
        point = 0
      pointer = ad.select_one('.adProduct_info_area__dTSZf > .adProduct_etc_box__UJJ90 > .adProduct_etc___brfw > a > .adProduct_count__EDNPm')
      if pointer != None:
        pointer = pointer.text.strip().replace('/n', '')
      else:
        pointer = 0
      jjim = ad.select_one('.adProduct_info_area__dTSZf > .adProduct_etc_box__UJJ90 > .adProduct_etc___brfw > .adProduct_num__t7R1x')
      if jjim != None:
        jjim = jjim.text.strip().replace('/n', '')
      else:
        jjim = 0
    else:
      not_ad = i.select_one('.product_inner__gr8QR')
      name = not_ad.select_one('.product_info_area__xxCTi > .product_title__Mmw2K > a').text.strip().replace('/n', '')
      money = not_ad.select_one('.product_info_area__xxCTi > .product_price_area__eTg7I > strong > .price > .price_num__S2p_v > em').text.strip().replace('/n', '')
      point = not_ad.select_one('.product_info_area__xxCTi > .product_etc_box__ElfVA > a > .product_grade__IzyU3')
      if point != None:
        point = float(point.text.strip().replace('/n', '').replace(' ','').replace('별점', '').replace('\t', ''))
      else:
        point = 0
      pointer = not_ad.select_one('.product_info_area__xxCTi > .product_etc_box__ElfVA > a > .product_num__fafe5')
      if pointer != None:
        pointer = pointer.text.strip().replace('/n', '').replace(' ','').replace('별점', '').replace('\t', '').replace('(', '').replace(')', '')
        if pointer.find('만') != -1:
          pointer = pointer.replace('만','000').replace('.','')
        else:
          pointer = pointer.replace(',', '')
      else:
        pointer = 0
      jjim = not_ad.select_one('.product_info_area__xxCTi > .product_etc_box__ElfVA > .product_etc__LGVaW > .product_num__fafe5')
      if jjim != None:
        jjim = jjim.text.strip().replace('/n', '').replace('(', '').replace(')', '')
        if jjim.find('만') != -1:
          jjim = jjim.replace('만','000').replace('.','')
        else:
          jjim = jjim.replace(',', '')
      else:
        jjim = 0
      # print(jjim)
    if float(point) >= 4.8 and int(pointer.replace(',', '')) >=  1000:
      print(f'이름 : {name}')
      print(f'가격 : {money}')
      print(f'평점 : {point}')
      print(f'평가수 : {pointer}')
      print(f'찜 : {jjim}')
    shop_data.append([name, money, point, pointer, jjim])
  with open(f'20241025/naver_market_{j+1}.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(title)
    for k in shop_data:
      writer.writerow(k)
# 제목, 금액, 평점, 평가수, 찜 정보를 1 ~ 5페이지까지 가져와서
   

# for _, d_list in enumerate(data):
#   data_list = d_list.select('div.box__component.box__component-itemcard')
#   if len(data_list):
#     for i in data_list:
#       name = i.select_one('.link__item > span.text__item').text.strip().replace('\n', '')
#       money = int(i.select_one('.box__item-price > div.box__price-seller > strong.text.text__value').text.strip().replace('\n', '').replace(',', ''))
#       point = i.select_one('.box__information-score > .list__score > .list-item.list-item__awards > .box__seller-awards > .image__awards-points > .for-a11y')
#       if point != None:
#         point = point.text.strip().replace('\n', '')
#         point = int(point[point.find(" ") + 1:point.find(' ', point.find(' ') + 1) - 1])
#       else:
#         point = -1
#       pointer = i.select_one('.box__information-score > .list__score > .list-item.list-item__feedback-count > .text')
#       if pointer != None:
#         pointer = int(pointer.text.replace('(', '').replace(')', '').replace(',', '').strip())
#       else:
#         pointer = -1
#       if point >= 95 and money <= 1500000 and pointer >= 100:
#         print(f'이름 : {name}')
#         print(f'금액 : {money}')
#         print(f'만족도 : {point}')
#         print(f'평가자 수 : {pointer}')





















# # 검색해서 url 가져오는 함수
# text = naver_sreach()
# # print(text[:text.find('pagingIndex=')])
# fist_url = text[:text.find('pagingIndex=') + len('pagingIndex=')]
# last_url = text[text.find('pagingIndex=') + len('pagingIndex=') + 1:]
# for i in range(5):
#   if i >= 1:
#     time.sleep(10) 
#   url = fist_url + str(i+1) + last_url
#   wep = webdriver.Chrome()
#   wep.maximize_window() # 창 최대화 (전체화면)
#   wep.get(url)
#   time.sleep(10)

#   prev_height = wep.execute_script('return document.body.scrollHeight')
#   while True:
#     # 스크롤 내림
#     wep.execute_script('window.scrollTo(0, document.body.scrollHeight)')
#     # 화면 로딩 대기
#     time.sleep(1)
#     # 페이지가 로딩되면서 길어진 길이를 다시 가져옴
#     curr_height = wep.execute_script('return document.body.scrollHeight')
#     print('이전 길이 : ', prev_height)
#     # 이전 최대 높이와 현제 최대 높이 비교
#     if prev_height == curr_height:
#       break
#     prev_height = curr_height

#   soup = BeautifulSoup(wep.page_source, 'lxml')
#   with open(f'20241025/naver_market_{i+1}.html', 'w', encoding='utf-8') as f:
#     f.write(soup.prettify())
#   time.sleep(10)

  


# for i in range(5):
#   url = f'https://search.shopping.naver.com/search/all?adQuery=%EB%AC%B4%EC%84%A0%20%EB%A7%88%EC%9A%B0%EC%8A%A4&origQuery=%EB%AC%B4%EC%84%A0%20%EB%A7%88%EC%9A%B0%EC%8A%A4&pagingIndex={i + 1}&pagingSize=40&productSet=total&query=%EB%AC%B4%EC%84%A0%20%EB%A7%88%EC%9A%B0%EC%8A%A4&sort=rel&timestamp=&viewType=list'
#   wep = webdriver.Chrome()
#   wep.maximize_window() # 창 최대화 (전체화면)
#   wep.get(url)
#   time.sleep(10)

#   soup = BeautifulSoup(wep.page_source, 'lxml')
#   with open(f'20241025/naver_market_{i+1}', 'w', encoding='utf-8') as f:
#     f.write(soup.prettify())