# naver 파일저장
# 리솜리조트 파일저장
import requests

target_url = [
  # 'http://www.resom.co.kr/resom/main/main.asp',
  # 'http://www.naver.com',
  'http://www.coupang.com/',
  ]
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}

for url in target_url:
  res = requests.get(url, headers=header)
  first_name = url.index('.') + 1
  last_name = url.find('.', first_name + 1)
  print(res.status_code)
  if res.status_code == 200:
    print(f'{url[first_name: last_name]} 읽어 오기')
    # print(res.text)
    with open(f'{url[first_name: last_name]}_stu.html', 'w', encoding='utf-8') as f:
      f.write(res.text)