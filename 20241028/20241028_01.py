import oracledb
import cx_Oracle

conn = oracledb.connect(user="ora_user", password='1111', dsn='localhost:1521/xe')
# 연결확인
print(conn.version)

# sql 실행창 오픈
cursor = conn.cursor()
# sql = 'select count(*) from member'
# cursor.execute(sql)
# 검색된 데이터 호출
# count1 = cursor.fetchone()
# print('개수 : ', count1)
sql = 'select * from member'
cursor.execute(sql)
rows = cursor.fetchall()

for i in rows:
  for j in i:
    print(j, end='\t')
  print()

# 여러개 데이터 갬색된 내용 호출

conn.close()