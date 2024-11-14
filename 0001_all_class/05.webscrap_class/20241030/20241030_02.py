import random
import oracledb

def connect():
  user = 'ora_user'
  password = '1111'
  dsn = 'localhost:1521/xe'
  try:
    conn = oracledb.connect(user = user, password=password, dsn=dsn)
  except Exception as e: print('예외 발생 : ', e)
  return conn


conn = connect()
cursor = conn.cursor()

user_id = input('아이디를 입력하세요. >> ') # eee
user_pw = input('패스워드를 입력하세요. >> ') # 2222

sql = 'update member set pw=:pw where id=:id'
cursor.execute(sql, id=user_id, pw=user_pw)
conn.commit()

print('파일이 수정되었습니다.')

conn.close()


# a_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# a = random.randrange(0, 10000)

# ran_num = f'{a:04}'

# print(ran_num)

# print(f'{a:04}')

