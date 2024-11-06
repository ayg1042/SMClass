import oracledb

# 학생성적 출력

# sqldeveloper 실행
conn = oracledb.connect(user="ora_user", password='1111', dsn='localhost:1521/xe')

# sql 창이 열림
cursor = conn.cursor()

# sql 작성, 실행
sql = 'select * from students'
cursor.execute(sql)
rows = cursor.fetchall()

titles = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수', '등록일']
print('')

for idx, i in enumerate(titles):
  if idx == 1:
    print(f'{i:12s}', end='\t')
  else:print(i, end='\t')
print()
print('--'*60)

for i in rows:
  for idx, j in enumerate(i):
    if idx == 6:
      print(f'{j:.2f}', end='\t')
    elif idx == 1:
      print(f'{j:12s}', end='\t')
    else:
      print(j, end='\t')
  print()