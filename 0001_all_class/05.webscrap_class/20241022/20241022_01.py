import requests
from bs4 import BeautifulSoup

url = 'https://news.naver.com/main/ranking/popularDay.naver'
user_agent = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}

res = requests.get(url, headers=user_agent)
res.raise_for_status() # 에러시 종료
print()

# soup 변환
soup = BeautifulSoup(res.text, 'lxml')

data = soup.select_one("#wrap > div.rankingnews._popularWelBase._persist > div.rankingnews_box_wrap._popularRanking")
news = data.select("div.rankingnews_box")
for new in news:
  print("언론사 이름 : ",new.select_one("strong.rankingnews_name").text)
  news_lists = new.select("ul.rankingnews_list>li")
  for idx, news_list in enumerate(news_lists):
    print(f"{idx+1} : ",news_list.select_one("div.list_content>a").text)



# 태그를 활용한 검색방법
# find, find_all <==> select_one, select
# print(soup.find('h2', {'class' : 'rankingnews_tit'}))
# print(soup.select_one('h2.rankingnews_tit'))
# print(soup.select_one('div#header'))


# html, css 파싱이 되어서 이쁘게 출력
# print(soup.prettify())