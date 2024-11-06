import oracledb

# 학생성적 출력

# sqldeveloper 실행

# db연결 함수 선언
def connections():
  try:
    conn = oracledb.connect(user="ora_user", password='1111', dsn='localhost:1521/xe')
    print('db연결 : ', conn.version)
  except Exception as e: print("예외발생 : ",e)
  return conn
# sql 창이 열림
conn = connections()
cursor = conn.cursor()

# search = input('검색할 이름을 입력하세요. : ')

# employees에서 이름이 a가 포함되어있는 모든 컬럼 출력
# sql = "select * from employees where emp_name like '{}'"
# sql = "select * from employees where emp_name like ':1'"
# cursor.execute(sql, [search])

# 키워드
# sql = "select * from employees where emp_name like %a%"
# sql = "select * from employees where employee_id >= :search"
# 번호 순서
# sql = "select * from employees where employee_id >= :1"

# search = '%' + search + '%'
# sql = "select * from employees where emp_name like :search"
# cursor.execute(sql, search = search)

# 월급 4000 ~ 8000사이의 사원을 모두 출력하세요.
# sql = 'select * from employees where salary >= 4000 and salary <= 8000'

# 범위를 입력받아 그 사이의 사원을 출력하세요.
num1 = 1
num2 = 200
sql = 'select employee_id, emp_name, salary from employees where employee_id >= :1 and employee_id <= :2 order by employee_id'
cursor.execute(sql, [num1, num2])
rows = cursor.fetchall()

title = ['employee_id', 'emp_name', 'salary']
a_list = []
for i in rows:
  a_list.append(dict(zip(title, i)))
print(a_list)

conn.close()