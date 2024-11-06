import random
import oracledb
import smtplib
from email.mime.text import MIMEText
import func


while True:
  choice = func.screen()
  if choice == '1': # 로그인
    func.memLogin()
  elif choice == '2': # 비밀번호 찾기
    func.search_pw()
  elif choice == '3': # 회원가입
    pass
  elif choice == '4':
    break