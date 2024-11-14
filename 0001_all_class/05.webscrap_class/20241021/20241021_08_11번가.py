import requests
from bs4 import BeautifulSoup

url = 'https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&xfrom=main^gnb'
user_agent = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}

res = requests.get(url, headers=user_agent)
res.raise_for_status()
print()

# soup 변환
soup = BeautifulSoup(res.text, 'lxml')

# sreach = soup.find('div', {'id' : 'bestPrdList'}).find('h3')
# print(sreach.text)

# sreach = soup.find('div', {'id': 'bestPrdList'}).find('div', {'class':'pname'})
# print(sreach.p.text)
sreach = soup.find('div', {'id': 'bestPrdList'})
sreach_next = sreach.find('div', {'class' : 'viewtype catal_ty'}).find('ul', {"class" : 'cfix'}).find_all('li')
print(len(sreach_next))
# for i in sreach_next:
#   print(i.p.text)
for idx, i in enumerate(sreach_next):
  print('--' * 20)
  print(f'{idx + 1}번째 추천상품 타이틀 : {i.p.text}')
  if i.find("span", {"class":'price_detail'}).find('s', {'class':'normal_price'}) != None:
    print(f'{idx + 1}번째 추천상품 기본 가격 : {i.find("span", {"class":'price_detail'}).find('s', {'class':'normal_price'}).text}')
    print(f'{idx + 1}번째 추천상품 할인 가격 : {i.find("span", {"class":'price_detail'}).find('strong', {'class':'sale_price'}).text}원')
  else:
    print(f'{idx + 1}번째 추천상품 기본 가격 : {i.find("span", {"class":'price_detail'}).find('strong', {'class':'sale_price'}).text}원')
  print('--' * 20)