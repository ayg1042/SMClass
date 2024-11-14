import requests
from bs4 import BeautifulSoup

url = 'https://www.melon.com/chart/index.htm'
user_agent = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}

res = requests.get(url, headers=user_agent)
res.raise_for_status() # 에러시 종료
print()

soup = BeautifulSoup(res.text, 'lxml')
# print(soup.prettify())

# 순위, 사진링크주소, 제목, 가수명
data = soup.select_one('#frm > div > table')
# print(data)

data_list = data.select('tr')
# print(len(data_list))
title = data_list[0]
title_list = []
for i in title:
  if (i.text).strip() != '':
    title_list.append((i.text).strip())
# print(title_list)
del data_list[0]

# print(data_list)
lines = []
for _, i in enumerate(data_list):
  line = []
  if i.select_one('td:nth-child(2) > div > span.rank') != None:
    # 랭킹
    line.append(i.select_one('td:nth-child(2) > div > span.rank').text.strip())
  # 이미지
  line.append(i.select_one('td:nth-child(4) > div > a > img')['src'])
  # 공정보
  line.append(i.select_one('td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text.strip())
  with open(f'20241022/melon/{line[0]}_{line[2].replace(' ', '').replace('?', '').replace('(', '').replace(')', '')}.jpg', 'wb') as f:
    re_img = requests.get(i.select_one('td:nth-child(4) > div > a > img')['src'])
    f.write(re_img.content)
  # 아티스트 정보
  for j in i.select('td:nth-child(6) > div > div > div.ellipsis.rank02 > a'):
    line.append(j.text.strip())
  # 엘범
  line.append(i.select_one('td:nth-child(7) > div > div > div > a').text.strip())
  lines.append(line)
print(len(lines))

with open('20241022/melon/melon_top100.txt', 'w', encoding='utf-8') as f:
  for i in lines:
    f.write(','.join(i) + '\n')

  


























# a = '안녕,반가워,고마워,사랑해'
# a_list = a.split(',')
# print(a_list)

# title = ['순위', '종목명', '검색비율', '현재가', '전일비', '등락률',
#          '거래량', '시가', '고가', '저가', 'PER', 'ROE']
# a = ','.join(title)
# with open('a.txt', 'w', encoding='utf-8') as f:
#   f.write(a)