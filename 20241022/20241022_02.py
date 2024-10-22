import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/'
user_agent = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}

res = requests.get(url, headers=user_agent)
res.raise_for_status() # 에러시 종료
print()

# soup 변환
soup = BeautifulSoup(res.text, 'lxml')

# 기준점
data = soup.select_one('#container > div.aside > div > div.aside_area.aside_popular')
# 인기검색종목
print(data.select_one('span').text)
# 1, 2, 3, 4, 5위
data_list = data.select('tbody > tr')
# print(len(data_list))
sum = 0
for i in data_list:
  sum += int(i.select_one('td').text.replace(',', '').strip())
  print(f'번호 : {i.select_one('em').text}, 종목 : {i.select_one('a').text}, 금액 : {i.select_one('td').text}')
  num = i.select_one('span.tah.p11.nv01').text if i.select_one('span.tah.p11.nv01') != None else i.select_one('span.tah.p11.red02').text
  num = num.replace('\t', '').replace('\n', '')
  print(f'변동값 : {(i.select_one('span.blind').text).replace('\n', '')}, {num}')

print(f'합계 : {sum:,d}원')

# print(soup.select_one('h3.h_popular>span').text)


# google
# print(soup.select_one('title'))
# print(soup.select_one('div.L3eUgb'))
# data = soup.select_one('div.L3eUgb')
# lists = data.select('div.o3j99')
# print(f'개수 : {len(lists)}')