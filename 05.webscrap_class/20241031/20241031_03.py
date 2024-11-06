import oracledb

def connects():
  user = 'ora_user'
  pw = '1111'
  dsn = 'localhost:1521/xe'
  try:
    conn = oracledb.connect(user=user, password=pw, dsn=dsn)
  except Exception as e : print(e)
  return conn

conn = connects()
cursor = conn.cursor()

sql = 'select * from chartable'
cursor.execute(sql)
rows = cursor.fetchall()

for row in rows:
  print(f'{row[1]}')
