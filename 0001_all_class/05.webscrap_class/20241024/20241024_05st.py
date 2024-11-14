# 매매가격이 낮은 5개, 전세가격이 낮은 5개를 출력하시오.

from bs4 import BeautifulSoup
from selenium import webdriver
import time

with open(f'20241024/naver.html', 'r', encoding='utf-8') as f:
  soup = BeautifulSoup(f, 'lxml')

data = soup.select_one("#complexOverviewList > div.list_contents > div.item_area > div.item_list.item_list--article")
data_list = data.select('div.item.false')

total = {
  '59':{'월세':[],'전세':[],'매매':[]},
  '84':{'월세':[],'전세':[],'매매':[]},
  '101':{'월세':[],'전세':[],'매매':[]},
  '72':{'월세':[],'전세':[],'매매':[]},
  '71':{'월세':[],'전세':[],'매매':[]}
  }

for i in data_list:
  point = i.select_one('.item_inner > .item_link')
  name = point.select_one('.item_title > .text').text.strip().replace('\n', '')
  t_type = point.select_one('.price_line > .type').text.strip().replace('\n', '')
  money_type = point.select_one('.price_line > .price > .slash')
  mm_type = point.select_one('div.info_area > p:nth-child(1) > span').text.strip()
  mm_type = mm_type[mm_type.find('/') + 1:mm_type.find(',') - 2]
  # 월세 타입 검사
  if money_type == None:
    money = point.select_one('.price_line > .price').text.strip().replace('\n', '').replace('\t', '')
    if money.find('억') != -1:
      money = money.replace('억', '')
      if money.find(',') != -1:
        money += '0000'
        money = money.replace(',', '')
      else:
        money += '00000000'
        money = money.strip()
  else:
    money = point.select_one('.price_line > .price').text.strip().replace('\n', '').replace('\t', '')
    money_1 = money[:money.find('/')].replace(' ', '').strip()
    # 억 단위 검사
    if money_1.find('억') != -1:
      money_1 = money_1.replace('억', '')
      # 천 단위 검사
      if money_1.find(',') != -1:
        money_1 += '0000'
        money_1 = money_1.replace(',', '')
      else:
        money_1 += '00000000'
        money_1 = money_1.strip()
    money_2 = money[money.find('/'):].replace('/', '').strip()
  money.find(' ')
  
  if t_type != '월세':
    total[mm_type][t_type].append({'이름':name, '타입':t_type, '가격':int(money.replace(' ', ''))})
  else:
    total[mm_type][t_type].append({'이름':name, '타입':t_type, '보증금':int(money_1.replace(' ', '')), '월세':int(money_2.replace(' ', ''))})

  # if mm_type == '84':
  #   if t_type == '매매':
  #     farsa_mm.append({'이름':name, '타입':t_type, '가격':int(money.replace(' ', ''))})
  #   elif t_type == '전세':
  #     farsa_mm.append({'이름':name, '타입':t_type, '가격':int(money.replace(' ', ''))})
  #   elif t_type == '월세':
  #     farsa_mm.append({'이름':name, '타입':t_type, '보증금':int(money_1.replace(' ', '')), '월세':int(money_2.replace(' ', ''))})
  # elif mm_type == '101':
  #   if t_type == '매매':
  #     bak_mm.append({'이름':name, '타입':t_type, '가격':int(money.replace(' ', ''))})
  #   elif t_type == '전세':
  #     bak_mm.append({'이름':name, '타입':t_type, '가격':int(money.replace(' ', ''))})
  #   elif t_type == '월세':
  #     bak_mm.append({'이름':name, '타입':t_type, '보증금':int(money_1.replace(' ', '')), '월세':int(money_2.replace(' ', ''))})
  # elif mm_type == '59':
  #   if t_type == '매매':
  #     ogu_mm.append({'이름':name, '타입':t_type, '가격':int(money.replace(' ', ''))})
  #   elif t_type == '전세':
  #     ogu_mm.append({'이름':name, '타입':t_type, '가격':int(money.replace(' ', ''))})
  #   elif t_type == '월세':
  #     ogu_mm.append({'이름':name, '타입':t_type, '보증금':int(money_1.replace(' ', '')), '월세':int(money_2.replace(' ', ''))})

print('--' * 60)
print('정렬 전')
print('--' * 60)
print(total['101'])
print('--' * 60)
print(total['59'])
print('--' * 60)
print(total['71'])
print('--' * 60)
print(total['72'])
print('--' * 60)
print(total['84'])

# for i in bak_mm:
#   print(i['타입'])
# for i in range(20):
#   if ogu_mm[i]['타입'] == '전세':
#     print(f'이름 : {ogu_mm[i]['이름']}, 거래 타입 : {ogu_mm[i]['타입']}, 가격 : {ogu_mm[i]['가격']:,d}원')
#   if ogu_mm[i]['타입'] == '월세':
#     print(f'이름 : {ogu_mm[i]['이름']}, 거래 타입 : {ogu_mm[i]['타입']}, 가격 : {ogu_mm[i]['가격']:,d}원')
#   if ogu_mm[i]['타입'] == '매매':
#     print(f'이름 : {ogu_mm[i]['이름']}, 거래 타입 : {ogu_mm[i]['타입']}, 가격 : {ogu_mm[i]['가격']:,d}원')
#   print('--' * 60)

# t_mm.sort(key = lambda x : x['가격'])
# t_gs.sort(key = lambda x : x['가격'])
# t_ws.sort(key = lambda x : x['보증금'])

# print('--' * 60)
# print('정렬 후')
# print('--' * 60)
# for i in range(5):
#   print(f'이름 : {t_mm[i]['이름']}, 거래 타입 : {t_mm[i]['타입']}, 가격 : {t_mm[i]['가격']:,d}원')
#   print(f'이름 : {t_gs[i]['이름']}, 거래 타입 : {t_gs[i]['타입']}, 가격 : {t_gs[i]['가격']:,d}원')
#   print(f'이름 : {t_ws[i]['이름']}, 거래 타입 : {t_ws[i]['타입']}, 보증금 : {t_ws[i]['보증금']:,d}원, 월세 : {t_ws[i]['월세']}')
#   print('--' * 60)

