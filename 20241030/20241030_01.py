import oracledb
import random

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def connect():
  user = 'ora_user'
  password = '1111'
  dsn = 'localhost:1521/xe'
  try:
    conn = oracledb.connect(user = user, password=password, dsn=dsn)
  except Exception as e: print('예외 발생 : ', e)
  return conn

def mail(pw_ran):
  smtpName = "smtp.naver.com"
  smtpPort = 587

  # 자신의 네이버메일주소,pw, 받는사람이메일주소
  # 전송 메일
  sendEmail = "ayg1044@naver.com"
  pw = "P2YLU86NFHF1"
  # 받는 메일
  recvEmail = "ayg1044@naver.com"
  title = "비밀번호 입니다."
  content = f"임시비밀번호 입니다. >> {pw_ran:04}"
  msg = MIMEMultipart()
  msg["Subject"] = title
  msg["From"] = sendEmail
  msg["To"] = recvEmail
  msg.attach(MIMEText(content))
  
  s = smtplib.SMTP(smtpName,smtpPort)
  s.starttls() # 보안인증
  s.login(sendEmail,pw)
  print(content)
  s.sendmail(sendEmail,recvEmail,msg.as_string())
  # print("msg : ")
  # print(msg.as_string())
  s.quit()
  print("메일이 발송되었습니다.!")





while True:
  print(' [ 커뮤니티 ] ')
  print('1. 로그인')
  print('2. 비밀번호 분실')
  print('3. 회원가입')
  print('-'*30)

  choice = input('원하는 번호를 입력하세요. >> ')

  if choice == '1':
    print(' [ 로그인 ] ')
    user_id = input('아이디를 입력하세요. >> ')
    user_pw = input('패스워드를 입력하세요. >> ')

    conn = connect()
    cursor = conn.cursor()
    sql = 'select * from member where id=:id and pw=:pw'
    cursor.execute(sql, id=user_id, pw=user_pw)
    row = cursor.fetchone()
    if row != None:
      print(f'로그인 성공! {row[2]} 님 환영합니다.')
    else:
      print('아이디가 또는 패스워드가 일치 하지 않습니다.')
    # 오라클 db에 접속해서 가져온다.
    conn.close()

    if user_id == 'aaa' and user_pw == '1111':
      pass
    else:
      pass

  elif choice == '2':
    print(' [ 비밀번호 찾기 ] ')
    search = input('해당 아이디를 입력하세요 >> ')
    # 아이디가 있는지 확인
    conn = connect()
    cursor = conn.cursor()
    sql = 'select * from member where id=:id'
    cursor.execute(sql, id=search)
    row = cursor.fetchone()
    print(row)
    if row != None:
      print('아이디가 존재합니다. 임시패스워드를 발급합니다.')
      # 1. 입시 비밀번호를 생성해서
      # 2. 이메일로 보냅니다.
      # 3. 아이디에 비밀번호를 임시비밀번호를 수정합니다.
      # 3. 임시번허로 로그인을 했을 경우 로그인 성공이 나타나도록 하세요.
      ran_pw = random.randrange(0, 10000)
      print(ran_pw)
      pw = f'{ran_pw:04}'
      mail(ran_pw)
      sql = 'update member set pw=:pw where id=:id'
      cursor.execute(sql, pw=pw, id=search)
      conn.commit()
      print('변경 되었습니다.')
      conn.close()
    else:
      print('없는 아이디 입니다.')
  elif choice == '3':
    pass
  elif choice == '0':
    break