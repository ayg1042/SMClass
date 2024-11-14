import requests
from bs4 import BeautifulSoup

url = 'http://www.melon.com/index.htm'
user_agent = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}

res = requests.get(url, headers=user_agent)
res.raise_for_status()
print()

# soup 변환
soup = BeautifulSoup(res.text, 'lxml')
# print(soup.prettify())

sreach = soup.find('div', {'class' : 'hot_issue'})
# print(sreach.prettify())
deep = sreach.find_all('ul', {'class': 'sub_list'})
# print(deep)
# print(len(deep))
test1 = deep[0].find_all('dl')

# print(test1[0].find('span', {'class' : 'title'}).text)

for f_indx,i in enumerate(deep):
  print('--' * 30)
  test = i.find_all('dl')
  print('--' * 30)
  for idx, j in enumerate(test):
    print(j.find('span', {'class' : 'title'}).text)
    print(f'img url = {j.find("img")["src"]}')
    with open(f'20241021/{f_indx + 1}_{idx + 1}_{(j.find("span", {"class" : "title"}).text).replace(' ', '')}.jpg', 'wb') as f:
      re_img = requests.get(j.find('img')['src'])
      f.write(re_img.content)
  # for j in i:
  #   print(f'{j.find('span', {'class' : 'title'}).text}')