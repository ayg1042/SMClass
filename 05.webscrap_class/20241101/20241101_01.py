import oracledb
import datetime



def connects():
  user = 'ora_user'
  pw = '1111'
  dsn = 'localhost:1521/xe'
  try:
    conn = oracledb.connect(user=user, password=pw, dsn=dsn)
  except Exception as e : print(e)
  return conn


# sql = "select count(*) no,a.department_id dept,\
#   department_name deptname from employees a, departments b \
#     where a.department_id = b.department_id and a.department_id=50 \
#       group by a.department_id,department_name"
# cursor.execute(sql)
# row = cursor.fetchone()


def member_count():
  conn = connects()
  cursor = conn.cursor()
  sql = 'select * from mem'
  cursor.execute(sql)
  rows = cursor.fetchall()
  conn.close()
  return len(rows)

def login_fun(user_id, user_pw):
  conn = connects()
  cursor = conn.cursor()
  sql = 'select * from mem where id=:user_id and pw=:user_pw'
  cursor.execute(sql, user_id = user_id, user_pw = user_pw)
  user_data = cursor.fetchone()
  conn.close()
  if user_data == None:
    return -1
  else:
    return user_data

def member_add():
  now_year = datetime.datetime.now().year
  id = input('아이디를 입력하세요. >> ')
  pw = input('비밀번호를 입력하세요. >> ')
  name = input('이름을 입력하세요. >> ')
  birth = input('생일을 입력하세요. (ex -> 20240101)>> ')
  # ex) 20020312
  age = now_year - int(birth[:4]) # 나이 자동계산
  gender = input('성별을 입력하세요. (Male, Female)>> ')
  hobby = input('취미를 입력하세요. >> ')

  my_list = [id, pw, name, age, birth, gender, hobby]

  conn = connects()
  cursor = conn.cursor()
  # sql = 'insert into mem(id, pw, name, age, birth, gender, hobby) values (:1, :2, :3, :4, :5, :6, :7)'
  # cursor.executemany(sql, my_list)
  # sql = 'insert into mem(id, pw, name, age, birth, gender, hobby) values (:id, :pw, :name, :age, :birth, :gender, :hobby)'
  # cursor.executemany(sql, id=id, pw=pw, name=name, birth=birth, age=age, gender=gender, hobby=hobby)
  # conn.commit()
  sql = "insert into mem (id,pw,name,age,birth,gender,hobby) values (:id,:pw,:name,:age,:birth,:gender,:hobby)"
  cursor.execute(sql,id=id,pw=pw,name=name,age=age,birth=birth,gender=gender,hobby=hobby)
  conn.commit()
  conn.close()

def update_user():
  conn = connects()
  cursor = conn.cursor()
  id = 'aaa'
  sql = 'select * from mem where id=:id'
  cursor.execute(sql, id=id)
  row = cursor.fetchone()
  print(f'현재 취미 : {row[6]}')
  hobby = input('수정할 hobby를 입력하세요 >> ')
  sql = 'update mem set hobby = :hobby where id=:id'
  cursor.execute(sql, hobby=hobby, id=id)
  conn.commit()
  conn.close()
  print('수정되었습니다.')


## 회원수 확인값을 리턴하세요.
user_data = None
while True:
  all_member = member_count()

  print(' [ 커뮤니티 ] ')
  print(f'현재 회원수 : {all_member}')
  print()
  print(' 1. 로그인 ' if user_data == None else ' 1. 로그아웃')
  print(' 2. 회원가입')
  print(' 3. 정보수정')
  print(' 4. 종료')

  choice = input('번호를 입력하세요. >> ')
  if choice == '1':
    if user_data == None:
      id = input('ID를 입력하세요. >> ')
      pw = input('PW를 입력하세요. >> ')
      user_data = login_fun(id, pw)
      if user_data != -1:
        print(f'{user_data[2]}님 어서오세요.')
      else:
        print('로그인 실패 했습니다.')
    else:
      user_data = None
      print('로그아웃 되었습니다.')
  elif choice == '2':
    member_add()
  elif choice == '3':
    update_user()
  elif choice == '4':
    break



