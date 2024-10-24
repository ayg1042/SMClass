# 지마켓
from selenium import webdriver
from selenium.webdriver.common.by import By as by
from selenium.webdriver.common.keys import Keys as keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests, random
from bs4 import BeautifulSoup


# selenium 화면을 숨김처리
# url = ''
# browser = webdriver.Chrome()
# browser.maximize_window()
# browser.get(url)

# 노트북 검색 된 사이트 1, 2, 3페이지 에서
# 만족도 95 이상, 금액 1500000 이하, 평가수 100이상

# 페이지 다운
# for i in range(3):
#   url = f'https://www.gmarket.co.kr/n/search?keyword=%EB%85%B8%ED%8A%B8%EB%B6%81&k=61&p={i + 1}'
#   wep = webdriver.Chrome()
#   wep.maximize_window() # 창 최대화 (전체화면)
#   wep.get(url)
#   time.sleep(10)

#   soup = BeautifulSoup(wep.page_source, 'lxml')
#   with open(f'20241024/gmarket_{i+1}', 'w', encoding='utf-8') as f:
#     f.write(soup.prettify())
  
from bs4 import BeautifulSoup
from selenium import webdriver
import time
# 페이지 다운

def page_down(url, get_range):
  for i in range(get_range):
    url += i + 1
    wep = webdriver.Chrome()
    wep.maximize_window() # 창 최대화 (전체화면)
    wep.get(url)
    time.sleep(10)

    soup = BeautifulSoup(wep.page_source, 'lxml')
    with open(f'20241024/gmarket_{i+1}', 'w', encoding='utf-8') as f:
      f.write(soup.prettify())


# 요구사항
# 노트북 검색 된 사이트 1, 2, 3페이지 에서
# 만족도 95 이상, 금액 1500000 이하, 평가수 100이상

if __name__ == '__main__':

  # url = 'https://www.gmarket.co.kr/n/search?keyword=%EB%85%B8%ED%8A%B8%EB%B6%81&k=61&p='
  # page_down(url, 3)

  for page in range(3):
    with open(f'20241024/gmarket_{page + 1}.html', 'r', encoding='utf-8') as f:
      soup = BeautifulSoup(f, 'lxml')

    print(f'{page + 1}. 페이지')
    data = soup.select('#section__inner-content-body-container > div.section__module-wrap')
    for _, d_list in enumerate(data):
      data_list = d_list.select('div.box__component.box__component-itemcard')
      if len(data_list):
        for i in data_list:
          name = i.select_one('.link__item > span.text__item').text.strip().replace('\n', '')
          money = int(i.select_one('.box__item-price > div.box__price-seller > strong.text.text__value').text.strip().replace('\n', '').replace(',', ''))
          point = i.select_one('.box__information-score > .list__score > .list-item.list-item__awards > .box__seller-awards > .image__awards-points > .for-a11y')
          if point != None:
            point = point.text.strip().replace('\n', '')
            point = int(point[point.find(" ") + 1:point.find(' ', point.find(' ') + 1) - 1])
          else:
            point = -1
          pointer = i.select_one('.box__information-score > .list__score > .list-item.list-item__feedback-count > .text')
          if pointer != None:
            pointer = int(pointer.text.replace('(', '').replace(')', '').replace(',', '').strip())
          else:
            pointer = -1
          if point >= 95 and money <= 1500000 and pointer >= 100:
            print(f'이름 : {name}')
            print(f'금액 : {money}')
            print(f'만족도 : {point}')
            print(f'평가자 수 : {pointer}')