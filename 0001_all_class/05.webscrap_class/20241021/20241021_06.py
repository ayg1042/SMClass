import requests
from bs4 import BeautifulSoup

url = 'https://news.naver.com/main/ranking/popularDay.naver'
User_Agent = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}
res = requests.get(url, headers=User_Agent)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')
print()

news_list = soup.find('div', {'class':'rankingnews_box_wrap'}).find_all('div', {'class':'rankingnews_box'})
print(len(news_list))
for fr_idx,i in enumerate(news_list):
  print('--' * 30)
  print(f'{fr_idx + 1} 번째 타이틀 : {i.find('strong', {'class': 'rankingnews_name'}).text}')
  sub_list = i.find('ul', {'class': 'rankingnews_list'}).find_all('li')
  for idx, j in enumerate(sub_list):
    print(f'{idx + 1} 번째 타이틀 : {j.find('a', {'class':"list_title nclicks('RBP.rnknws')"}).text}')
  print('--' * 30)


# news_list = soup.find('div', {'class':'rankingnews_box_wrap'}).find('div', {'class':'rankingnews_box'})
# title = news_list.find('strong', {'class': 'rankingnews_name'}).text
# sub_title = news_list.find('ul', {'class': 'rankingnews_list'}).find_all('li')
# print("News_title : ", title)
# print('sub_title_range', len(sub_title))
# for idx,i in enumerate(sub_title):
#   print(f'{idx + 1} 번째 타이틀 : {i.find('a', {'class':"list_title nclicks('RBP.rnknws')"}).text}')