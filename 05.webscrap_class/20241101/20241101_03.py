import oracledb
import datetime
# 학생성적프로그램
# 1. 학생성적입력
# 2. 학생성적출력
# 3. 학생성적검색
# students 테이블을 사용하여
# 시퀀스 students_seq생성
# 김유신, 99, 98, 96 합계, 평균, 등수, 입력일
#######
def connects():
  user = 'ora_user'
  pw = '1111'
  dsn = 'localhost:1521/xe'
  try:
    conn = oracledb.connect(user=user, password=pw, dsn=dsn)
  except Exception as e : print(e)
  return conn

def add_data():
  conn = connects()
  name = input('학생 이름을 입력하세요. >> ')
  kor = int(input('국어점수를 입력하세요. >> '))
  eng = int(input('영어점수를 입력하세요. >> '))
  math = int(input('수학점수를 입력하세요. >> '))
  total = kor + eng + math
  avg = total/3
  rank = 0
  d_date = datetime.datetime.now()

  cursor = conn.cursor()
  sql = 'insert into students(no, name, kor, eng, math, total, avg, rank, sdate) values(students_seq.nextval, :name, :kor, :eng, :math, :total, :avg, :rank, :d_date)'
  cursor.execute(sql, name=name, kor=kor, eng=eng, math=math, total= total, avg=avg, rank=rank, d_date=d_date)
  conn.commit()
  conn.close()
  print('입력이 완료되었습니다.')

def show_data():
  conn = connects()
  cursor = conn.cursor()
  sql = 'select * from students order by no'
  cursor.execute(sql)
  data_list = cursor.fetchall()
  print(f'번호\t이름{'':10}\t국어\t영어\t수학\t합계\t평균\t등수\t입력일')
  print('-*-'*30)
  for data in data_list:
    for idx, i in enumerate(data):
      if idx == 1:
        print(f'{i:10}', end='\t')
      elif idx == 6:
        print(f'{round(i, 2)}', end='\t')
      else:
        print(f'{i}', end='\t')
    print()

def sreach_data():
  print(' [ 학생성적 검색 ] ')
  name = input('검색할 학생 이름을 입력하세요 >> ')
  conn = connects()
  cursor = conn.cursor()
  sql = 'select * from students where name = :name'
  cursor.execute(sql, name=name)
  data = cursor.fetchone()
  print(f'번호\t이름{'':10}\t국어\t영어\t수학\t합계\t평균\t등수\t입력일')
  print('-*-'*30)
  if data == None: return -1
  for idx, i in enumerate(data):
    if idx == 1:
      print(f'{i:10}', end='\t')
    elif idx == 6:
      print(f'{round(i, 2)}', end='\t')
    else:
      print(f'{i}', end='\t')
  print()

while True:
  print(' [ 학생성적 프로그램 ] ')
  print(' 1. 학생성적입력')
  print(' 2. 학생성적출력')
  print(' 3. 학생성적검색')
  choice = input('원하는 번호를 선택하세요. >> ')

  if choice == '1':
    add_data()
  elif choice == '2':
    show_data()
  elif choice == '3':
    chek = sreach_data()
    if chek == -1:
      print('검색에 실패 했습니다.')
  elif choice == '4':
    break