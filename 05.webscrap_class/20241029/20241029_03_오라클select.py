import oracledb

# 학생성적 출력

# sqldeveloper 실행
conn = oracledb.connect(user="ora_user", password='1111', dsn='localhost:1521/xe')

# sql 창이 열림
cursor = conn.cursor()

num1 = input('숫자를 입력하세요')

n_list = num1.split(',')

# sql 작성, 실행
sql = 'select * from students where no in (:1, :2, :3)'
# excute 함수 : 리스트 값 전달.
cursor.execute(sql, n_list)

rows = cursor.fetchall()

for i in rows:
  print(i)

conn.close()