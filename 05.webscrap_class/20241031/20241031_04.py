import oracledb

def connects():
  user = 'ora_user'
  pw = '1111'
  dsn = 'localhost:1521/xe'
  try:
    conn = oracledb.connect(user=user, password=pw, dsn=dsn)
  except Exception as e : print(e)
  return conn

# 입력한 달 이상의 입사한 사원을 출력하세요.
d_day = input('숫자를 입력하세요. >> ')
if len(d_day) == 1:
  d_day = '0' + d_day

conn = connects()
cursor = conn.cursor()

sql = 'select * from employees where substr(hire_date, 4, 2) >= :day'
cursor.execute(sql, day = d_day)
rows = cursor.fetchall()
# print(rows)
if rows == None:
  print('잘못 입력되었습니다.')
else:
  for i in rows:
    print(i[4])
