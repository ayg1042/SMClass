import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/lastsearch2.naver'
user_agent = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}

res = requests.get(url, headers=user_agent)
res.raise_for_status() # 에러시 종료
print()

soup = BeautifulSoup(res.text, 'lxml')

data = soup.select_one('#contentarea > div.box_type_l > table')
stocks = data.select('tr')
print(len(stocks))

# 상단 타이틀 출력
tits = stocks[0].select("th")
title = []
for tit in tits:
  title.append(tit.text)
  print(tit.text, end='\t')
print()
print('--' * 40)

# print(stocks[2])
st_lists = []
for i in range(2, 50):
  st_list = []
  sts = stocks[i].select('td')
  for idx, st in enumerate(sts):
    s = ''
    if idx == 4:
      s = st.select_one('span').text
      s += st.select_one('span').next.next.next.next.text.strip()
      print(st.select_one('span').text, end='')
      print(st.select_one('span').next.next.next.next.text.strip())
    else:
      s = st.text.strip()
      print(st.text.strip())
    st_list.append(s)
  st_lists.append(st_list)
  print()
  print('-' * 80)

# print(st_lists)
# stock.txt에 저장
with open('stock.txt', 'w', encoding='utf-8') as f:
  for i in st_lists:
    f.write(','.join(i) + '\n')
  

# 주식 30개 출력






# chex_list = [
#   '<td class="blank_06" colspan="12"></td>',
#   '<td class="division_line" colspan="12"></td>',
#   '<td class="blank_08" colspan="12"></td>'
#   ]

# data = soup.select_one('#contentarea > div.box_type_l')
# title_list = data.select('table > tr > th')
# for i in title_list:
#   print(i.text, end='\t')
# print()
# data_list = data.select("table > tr")
# del data_list[0]
# del data_list[0]
# for i in data_list:
#   for j in i:
#     if str(j) not in chex_list:
#       # print(j)
#       print((j.text).replace('\n', '').replace('\t', '').replace(',', ''), end=' ')
#   print()
