import requests
from bs4 import BeautifulSoup

url = 'https://news.naver.com/main/ranking/popularDay.naver'
User_Agent = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}
res = requests.get(url, headers=User_Agent)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml') # html 전체를 가져온다.
print()
cont = soup.find('div', {'class', "rankingnews_box_wrap"})
rank_lists = cont.find_all('div', {'class' : 'rankingnews_box'})
print('개수 확인 하 기 : ', len(rank_lists))

# 파일에 1줄씩 저장하시오.
with open('20241021/news.text', 'w', encoding='utf-8') as f:
  for index, rank_list in enumerate(rank_lists):
    print(f'{index + 1}번째 언론사 타이틀 : ', rank_list.find('strong', {'class':'rankingnews_name'}).text)
    news = rank_list.find('ul', {'class':'rankingnews_list'})
    news_list = news.find_all('li')
    print('랭킹박스 안 뉴스 개수 : ', len(news_list))
    f.write(f'{index + 1}번째 언론사 타이틀 : {rank_list.find('strong', {'class':'rankingnews_name'}).text}\n')
    for idx, new in enumerate(news_list):
      print(f'{idx + 1} 번째 내용 : {new.find('a').text}')
      f.write(f'{idx + 1} 번째 내용 : {new.find('a').text}\n')