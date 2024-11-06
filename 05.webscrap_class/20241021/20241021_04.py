import requests
from bs4 import BeautifulSoup

url = 'https://news.naver.com/main/ranking/popularDay.naver'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}

res = requests.get(url, headers=header)
res.raise_for_status()

# html, css 정보를 가진 소스변경
soup = BeautifulSoup(res.text, 'lxml') # str -> html태그, css태그 사용될수 있는 형태로 변경
print(soup.title) # title 태그
print(soup.title.get_text()) # title 태그 안의 문자를 가져온다 text, get_test()

print(soup.a)
print(soup.a.next) # 해당 태그의 바로 안쪽 태그가 출력된다
print(soup.a.attrs) # 태그의 속성값 가져온다. dict 타입
print(soup.a['href']) # 태그의 href 가져온다.

# 특정정보 출력
# print(soup.find('div', attrs={'id': 'header'}))
# print(soup.find('h2', attrs={'class': 'rankingnews_tit'}).text) # 해당 값을 출력
print(soup.find_all('div')) # 모든 div 태그 검색
print(len(soup.find_all('div'))) # 모든 div태그 개수 출력



# 없는 태그 입력시 None
# test.text  없는 태그 입력시 에러

# soup 정보 저장
# with open('20241021/2.html', 'w', encoding='utf-8') as f:
#   # soup.prettify() : 소스가 정리되어 저장됨
#   f.write(soup.prettify())


# with open('20241021/1.html', 'w', encoding='utf-8') as f:
#   f.write(res.text)

# print(res.text)

