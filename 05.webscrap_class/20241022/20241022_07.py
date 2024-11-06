import os
import requests
from bs4 import BeautifulSoup
url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=9&backgroundColor="
headers = {
  "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
  'Accept-Language' : 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'
  }
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료
# print(res.text)
soup = BeautifulSoup(res.text,"lxml")
# print(soup.prettify())

# 제목, 금액, 평점, 평가수, 링크주소, 이미지주소
# 금액 90만원 이상, 평점 4.5 이상, 평가수 500명 이상 출력
data = soup.select_one('#productList')
data_list = data.select('li')
for i in data_list:
  name = i.select_one('a > dl > dd > div > div.name').text
  if i.select_one('a > dl > dd > div > div.price-area > div > div.price > em > strong') != None:
    money = i.select_one('a > dl > dd > div > div.price-area > div > div.price > em > strong').text
  else:
    money = '0'
  if i.select_one('a > dl > dd > div > div.other-info > div > span.star > em') != None:
    point = i.select_one('a > dl > dd > div > div.other-info > div > span.star > em').text
  else:
    point = '0'
  if i.select_one('a > dl > dd > div > div.other-info > div > span.rating-total-count') != None:
    point_count = i.select_one('a > dl > dd > div > div.other-info > div > span.rating-total-count').text
  else:
    point_count = '(0)'
  a_link = i.select_one('a')['href']
  img_link = i.select_one('a > dl > dt > img')['src']
  # print(point_count[1:-1])
  if int(money.replace(',', '')) >= 900000 and float(point) >= 4.5 and int(point_count[1:-1]) >= 500:
    print(f'상품명 : {name}\n가격 : {money}\n평점 : {point}\n평가수 : {point_count}\n링크주소 : https://www.coupang.com/{a_link}\n이미지주소 : https:{img_link}')
  print('--' * 50)