from selenium import webdriver
from selenium.webdriver.common.by import By as by
from selenium.webdriver.common.keys import Keys as keys
import time
import requests
from bs4 import BeautifulSoup

# for i in range(5):
#   url = f'https://www.yeogi.com/domestic-accommodations?keyword=%EA%B0%95%EB%A6%89&checkIn=2024-10-23&checkOut=2024-10-24&personal=2&freeForm=false&page={i + 1}'
#   browser = webdriver.Chrome()
#   time.sleep(5)
#   browser.get(url)
#   time.sleep(5)
#   soup = BeautifulSoup(browser.page_source, 'lxml')
#   # 파일로 저장
#   with open(f'20241023/yeogi_test_{i+1}.html', 'w', encoding='utf-8') as f:
#     f.write(soup.prettify())
# data = soup.select_one('#__next > div > main > section > div.css-1qumol3')

# # 파일로 불러오기
for j in range(5):
  with open(f'20241023/yeogi_test_{j + 1}.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'lxml')

  # 제목,평점,평가수,금액,이미지,링크주소
  data = soup.select_one('#__next > div > main > section > div.css-1qumol3')
  # print(data)
  data_list = data.select('a')
  print(len(data))
  print(len(data_list))
  # print(data_list[0].select_one('.css-8fn780 > h3').text)

  # 평점 9.0이상, 평가수 500이상, 금액 120,000이하
  print(f'{j+1} 번째 페이지 결과')
  print('--' * 60)

  for idx, i in enumerate(data_list):
    title = i.select_one('div > div.css-1by0ap6 > div.css-b0qdn7 > div > div > div.css-8fn780 > h3')
    point = float(i.select_one('div > div.css-1by0ap6 > div.css-b0qdn7 > div > div > div.css-1ar2n2o > div > span').text.strip())
    point_list = i.select_one('div > div.css-1by0ap6 > div.css-b0qdn7 > div > div > div.css-1ar2n2o > span')
    point_list = int(point_list.text[:point_list.text.find('명 평가')].strip().replace(',', ''))
    a_link = i['href']
    if i.select_one('div > div.css-7xiv94 > div.css-nl3cnv > img') != None:
      img = i.select_one('div > div.css-7xiv94 > div.css-nl3cnv > img')['src']
    else:
      img = ''
    if len(i.select('div.css-yeouz0')) > 1:
      for k in i.select('div.css-yeouz0'):
        if k != None:
          money_list = [ mz.text.strip().replace(',', '') for mz in k]
    else:
      if i.select_one('div.css-yeouz0 > span.css-5r5920') != None:
        money = int((i.select_one('div.css-yeouz0 > span.css-5r5920').text.strip()).replace(',', ''))
    # if point_list >= 500 and point >= 9.0 and money <= 120000:
    #   print(f'{idx + 1} 번 상품 목록 --------------------------------------------------')
    #   print('상품명 : ',title.text.strip())
    #   print('평점 : ',point)
    #   print(f'평가수 : {point_list:,d}')
    #   print(f'가격 : {money:,d}')
    #   print(f'이미지 : {img}')
    print(f'{idx + 1} 번 상품 목록 --------------------------------------------------')
    print('상품명 : ',title.text.strip())
    print('평점 : ',point)
    print(f'평가수 : {point_list:,d}')
    print(f'가격 : {money:,d}')
    print(f'이미지 : {img}')
    print(f'링크 : https://www.yeogi.com{a_link}')
  print('--' * 60)


# requests로 정보 가져오기
# url = 'https://www.yeogi.com/domestic-accommodations?keyword=%EA%B0%95%EB%A6%89&checkIn=2024-10-23&checkOut=2024-10-24&personal=2&freeForm=false'
# headers = {
#   "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
#   'Accept-Language' : 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'
#   }

# res = requests.get(url,headers=headers)
# soup = BeautifulSoup(res.text, 'lxml')

# with open('20241023/yeogi1.html', 'w', encoding='utf-8') as f:
#   f.write(soup.prettify())

# data = soup.select_one('#__next > div > main > section > div.css-1qumol3')
# print(data)
