# 웹 스크래핑 라이브러리
# pip install requests
# pip install beautifulsoup4
# pip install lxml

# 웹 크롤링
# 웹 크롤러(자동화 봇)이 일정 규칙에 따라 복수 개의 웹 페이지를 브라우징 하는 것

# 웹 스크래핑
# 웹 사이트 상에서 원하는 정보를 추출하여 수집하는 기술

import requests

res = requests.get('http://www.google.com/') # html 소스를 가져온다.
res = requests.get('http://www.naver.com/') # html 소스를 가져온다.
# res = requests.get('https://www.melon.com/index.htm')

# requests 정보를 가져올시 제이쿼리, 자바스크립트, 외부페이지, react, vue.. 비동기식으로 작동되는 소스는
# 가져오지 못함.

res.raise_for_status() # 에러시 종료
print('응답코드 : ',  res.status_code)
print('총 문자 길이 : ', len(res.text))

# 파일 저장
# f = open('a.html', 'w', encoding='utf-8')
# f.write(res.text)
# f.close()

# with open('b.html', 'w', encoding='utf-8') as f: # close() 하지 않아도 자동으로 닫힘
#   f.write(res.text)

# if res.status_code == 200:
#   print(res.text) # html 소스 출력
# else:
#   print('접근할 수 없습니다.')