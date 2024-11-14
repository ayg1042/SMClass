import smtplib
from email.mime.text import MIMEText
import random
import random
import oracledb
import smtplib


# 임시비밀번호 생성 함수선언
def random_pw():
  a = random.randrange(0, 10000) # 0 ~ 9999
  ran_num = f'{a:04}'
  print('랜덤 번호 : ', ran_num)
  return ran_num

# 메일발송 함수 선언
def emailSend(email):
  smtpName = 'smtp.naver.com'
  smtpPort = 587

  sendEmail = 'ayg1044@naver.com'
  pw = "P2YLU86NFHF1"
  recvEmail = email

  title = '[ 메일 발송 ] 임시 비밀번호 안내'
  ran_pw = random_pw()
  content = '임시 비밀번호 : ' + ran_pw

  msg = MIMEText(content)
  msg['Subject'] = title
  msg['From'] = sendEmail
  msg['To'] = recvEmail

  # 서버이름, 서버포트
  s = smtplib.SMTP(smtpName, smtpPort)
  s.starttls()
  s.login(sendEmail, pw)
  s.sendmail(sendEmail, recvEmail, msg.as_string())
  s.quit()
  return ran_pw

def connects():
  user='ora_user'
  pw = '1111'
  dsn = 'localhost:1521/xe'
  try:
    conn = oracledb.connect(user=user, password=pw, dsn=dsn)
  except Exception as e : print('에러 : ', e)
  return conn

def screen():
  print(' [ 커뮤니티 ] ')
  print(' 1. 로그인 ')
  print(' 2. 비밀번호 찾기 ')
  print(' 3. 회원가입 ')
  print(' 4. 프로그램 종료 ')

  choice = input('원하는 번호를 입력하세요. >> ')
  return choice

def memLogin():
  id = input('아이디를 입력하세요. >> ')
  pw = input('비밀번호를 입력하세요. >> ')

  conn = connects()
  cursor = conn.cursor()
  sql = 'select * from member where id=:id and pw=:pw'
  cursor.execute(sql, id=id, pw=pw)
  row = cursor.fetchone()
  conn.close()
  if row == None:
    print('아이디 또는 비밀번호가 일치하지 않습니다. ')
    return 0
  else:
    print(f'{row[2]} 님 환영합니다. ')
    print(' 어쩌구')
    print(' 어쩌구')
    print(' 어쩌구')
    print(' 어쩌구')

def search_pw():
  id = input('아이디를 입력하세요. >> ')

  conn = connects()
  cursor = conn.cursor()
  sql = 'select * from member where id=:id'
  cursor.execute(sql, id=id)
  row = cursor.fetchone()
  
  if row == None:
    print('없는 아이디 입니다.')
    return 0
  print(f'{row[0]} 아이디가 존재합니다.')
  input('메일을 보내려면 enter를 입력하세요.')
  ran_pw = emailSend(row[3])

  sql = 'update member set pw=:pw where id=:id'
  cursor.execute(sql, pw=ran_pw, id=id)
  conn.commit()
  conn.close()
