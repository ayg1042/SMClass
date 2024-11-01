




def operate(no):
  for i in range(no):
    print('한국어 인사 : 안녕하세요.')


if __name__ == '__main__':
  while True:
    print(' [ 외국어 인사 ] ')
    print('1. 한국어 인사')
    print('2. 일본어 인사')
    print('3. 영어 인사')
    print('4. 프랑스 인사')
    choice = input('원하는 번호를 입력하세요. >> ')
    count = input('원하는 반복회수를 입력하세요. >> ')
    if choice == '1':
      for i in range(int(count)):
        operate(int(count))
        print('영어 인사 : 헬로우, (Hello)')
    elif choice == '2':
      print('한국어 인사 : 안녕하세요.')
      print('일본어 인사 : 오하이요, (Ohayo)')
    elif choice == '3':
      print('한국어 인사 : 안녕하세요.')
      print('중국어 인사 : 니하오, (Ni Hau)')
    elif choice == '4':
      print('한국어 인사 : 안녕하세요.')
      print('중국어 인사 : 봉주르, (Bonjour)')