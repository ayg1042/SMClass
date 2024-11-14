# 평점 4.8 이상, 금액 : 17만원 이하
# 1.
# 호텔명 :
# 평점 :
# 금액 :
# -----------------

from bs4 import BeautifulSoup




if __name__=='__main__':
  with open('20241024/yanolja.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'lxml')
  
  data = soup.select_one('#__next > div > main > section > div.PlaceListBody_listContainer__2qFG1')
  # print(data)
  # print('--' * 30)
  data_list = data.select('div.PlaceListItemText_container__fUIgA')
  # print(data_list)
  print(len(data_list))

  hotels = []
  for indx, i in enumerate(data_list):
    # print(i)
    name = i.select_one('a > div.PlaceListItemText_area__3l67D > div.PlaceListItemText_contents__2GR73.place-content.PlaceListItemText_singlePrice__1aj9I > div.PlaceListTitle_container__qe7XH > strong').text.strip().replace('\n', '')
    point = i.select_one('a > div.PlaceListItemText_area__3l67D > div.PlaceListItemText_contents__2GR73.place-content.PlaceListItemText_singlePrice__1aj9I > div.PlaceListItemText_extraInfos__3Bp2B > div > span.PlaceListScore_rating__3Glxf')
    if point != None:
      point = float(point.text.replace('\n', '').strip())
    else:
      point = -1
    money = i.select_one('a > div.PlaceListItemText_area__3l67D > div.PlaceListItemText_contents__2GR73.place-content.PlaceListItemText_singlePrice__1aj9I > div.PlaceListItemText_prices__2_1nN > div > div.PlacePriceInfoV2_bottomInfo__2h62q > span > span.PlacePriceInfoV2_discountPrice__1PuwK')
    if money != None:
      money = int(money.text.replace('\n', '').strip().replace(',', ''))
    else:
      money = -1
    hotels.append({'호텔':name, '평점':point, '금액':money})

  # 조건에 맞는 개수
  # 조건에 맞지 않는 개수
  # 예외처리 개수
  count = 0
  n_count = 0
  for idx, i in enumerate(hotels):
    if i['평점'] >= 4.8 and 0 < i['금액'] <= 170000:
      count += 1
      print(f'{idx}번')
      print(f'호텔 명 : {i['호텔']}')
      print(f'평점 : {i['평점']}')
      print(f'금액 : {i['금액']:,d}')
    if i['평점'] == -1 or i['금액'] == -1:
      n_count += 1
  
  print(f'총 호텔 개수 : {len(hotels)}')
  print(f'조건에 맞는 개수 : {count}')
  print(f'조건에 맞지 않는 개수 : {len(hotels) - count - n_count}')
  print(f'예외처리 된 개수 : {n_count}')
  
  hotels.sort(key = lambda x : x['금액'])
  print(hotels)