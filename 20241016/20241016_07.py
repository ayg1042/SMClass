print('안녕')
nstr = input('숫자만 입력 가능합니다 >> ')
if nstr.isdigit():
  print('숫자로 변환이 가능합니다.')
else:
  print('숫자로 변환 안됨')

# try-except : 프로그램 예외를 처리하는 명령어
# try:
#   num = int(nstr)
#   print('입력된 숫자로 100 나누기', 100/num)
# except:
#   print('숫자로 변환 안됨')