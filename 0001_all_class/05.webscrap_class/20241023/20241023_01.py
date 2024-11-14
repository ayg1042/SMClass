import os
import requests
from bs4 import BeautifulSoup
import time, csv

url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {
  "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
  'Accept-Language' : 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'
  }
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료
# print(res.text)
soup = BeautifulSoup(res.text,"lxml")

# print(soup.prettify())

data = soup.select_one('#contentarea > div.box_type_l > table')
data_list = data.select('tr')
# print(len(data_list))

# 1. 상단 타이틀
title_list = [i.text for i in data_list[0].select('th')]
print(title_list) # 12개

# 2. 
print(data_list[1].select('td')) # 항목 1개
print(len(data_list[2].select('td'))) # 12개

d_list = []
test = []
with open('20241023/주식정보.csv', 'w', encoding='utf-8-sig', newline='') as f:
  writer = csv.writer(f)
  writer.writerow(title_list)
  for i in data_list:
    data = i.select('td')
    if len(data) > 3:
      for j in data:
        d_list.append(j.text.replace('\t', '').replace('\n', ''))
      writer.writerow(d_list)
      d_list = []
print(test)

# 30개 주식정보를 csv파일로 저장하시오.
# with open('20241023/주식정보.csv', 'w', encoding='utf-8-sig') as f:
#   writer = csv.writer(f)
#   writer.writerow()

# st_list = [i.text.strip().replace('\t', '').replace('\n', '') for i in data_list[2].select('td')]
# print(st_list)