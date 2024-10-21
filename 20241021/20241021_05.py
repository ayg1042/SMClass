import requests
from bs4 import BeautifulSoup

url = 'https://news.naver.com/main/ranking/popularDay.naver'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}

res = requests.get(url, headers=header)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

print()

print(soup.title) # 제일먼저 찾아지는 것을 출력
print(soup.find("title")) # 특정위치의 태그와 속성을 가지고 찾아줌
print(soup.find("div",{"class":"rankingnews_box_wrap"}))
newLists = soup.find("div",{"class":"rankingnews_box_wrap"}).find("div",{"class":"rankingnews_box"})
print("여러개 개수 확인 : ",len(newLists))
print(1, '=' * 90)
print(newLists)
print(1, '=' * 90)
# next : 검색태그 다윔뒤에 오는 태그를 찾아준다.
# next_sibling : 검색태그의 형제관계의 다음태그
print(newLists.next_sibling.next_sibling)
# # find : 1개 검색
# rankingnews_wrap = soup.find("div",{"class":"rankingnews_box_wrap"})
# # find_all : 여러개 검색
# rankingnews_boxs = rankingnews_wrap.find_all("div",{"class":"rankingnews_box"})
# print(len(rankingnews_boxs))
# # print(len(soup.find_all("div",{"class":"rankingnews_box"})))










# rankingnews_wrap = soup.find('div', {'class': 'rankingnews_box_wrap'})
# find_all : 여러개 검색
# news_lists = rankingnews_wrap.find_all('div', {'class': 'rankingnews_box'})
# print('개수 확인 : ', len(news_lists))

# print(type(rankingnews_wrap))
# print(type(news_lists))

# for news in news_lists:
#   print(type(news))
#   print(news.find('strong', {'class':'rankingnews_name'}).text)


# find = 특정위치의 태그를 출력
# find('div', {'class': 'rankingnews_box_wrap'}) # 태그와 

# print(soup.find('div', {'class': 'rankingnews_box_wrap _popularRanking'}))
# print(len(soup.find_all('div', {'class': 'rankingnews_box'})))

# 특정정보 출력
# print(soup.find('div', attrs={'id': 'header'}))
# print(soup.find('h2', attrs={'class': 'rankingnews_tit'}).text) # 해당 값을 출력
# print(soup.find_all('div')) # 모든 div 태그 검색
# print(len(soup.find_all('div'))) # 모든 div태그 개수 출력


# a = '안녕하세요. 반갑습니다. 파이썬 수업입니다.'

# search = '파이썬'

# print(a.find(search))
# print(a[a.find(search):a.find(search) + len(search)])