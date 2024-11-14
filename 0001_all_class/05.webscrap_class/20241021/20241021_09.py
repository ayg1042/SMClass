import requests
from bs4 import BeautifulSoup

url = 'http://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EC%98%81%ED%99%94'
user_agent = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}

res = requests.get(url, headers=user_agent)
res.raise_for_status()
print()

# soup 변환
soup = BeautifulSoup(res.text, 'lxml')
with open('20241021/screen.html', 'w', encoding='utf-8') as f:
  f.write(soup.prettify())

# print(soup.prettify())

sreach = soup.find('body').find('div', {'id':'daumContent'}).find('div', {'id': 'mArticle'}).find('c-flicking', {'id': 'mor_history_id_0'})
sreach2 = soup.find('body').find('div', {'id':'daumContent'}).find('div', {'id': 'mArticle'}).find('c-flicking-item')
title = sreach2.find_all('c-title')
content = sreach2.find_all('c-contents-desc')
# print(sreach.prettify())
# print(sreach2.prettify())
# print(sreach_deep)
cont = []
tit = []
for i in content:
  i = str(i)
  start = i.find('slot="contents"> ')
  start_len = len('slot="contents"> ')
  last = i.find(' </c-contents-desc>')
  cont.append(i[start + start_len: last])

for i in title:
  i = str(i)
  start = i.find('slot="title"> ')
  start_len = len('slot="title"> ')
  last = i.find('</c-title>')
  tit.append(i[start + start_len:last])

for i, j in zip(tit, cont):
  print(f'영화 이름 : {i}')
  print(f'{j}')