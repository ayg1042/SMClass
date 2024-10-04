





if __name__=="__main__":

  s_list = []
  no = 1
  while True:
    # 이름, 국어, 영어, 수학 -> 번호, 이름, 국어, 영어, 수학, 합계, 평균
    name = input('이름을 입력하세요. (종료 0)')
    if name == '0': break
    kor = int(input('국어 점수를 입력하세요'))
    eng = int(input('영어 점수를 입력하세요'))
    math = int(input('수학 점수를 입력하세요'))
    print(f'번호 : {no}, 이름 : {name}, 국어 : {kor}, 영어 : {eng}, 수학 : {math},\
          합계 : {kor + eng + math}, 평균 : {(kor + eng + math)/3:.2f}')
    no += 1

  # 두수를 입력받아, 더하기, 곱하기, 빼기, 나누기
  # while True:
  #   num1 = int(input('숫자를 입력하세요. '))
  #   num2 = int(input('숫자를 입력하세요. (종료 : 0) '))
  #   if not num2: break
  #   print('[ 두수의 사칙연산 ]')
  #   print('-' * 50)
  #   print('1. 두수 더하기')
  #   print('2. 두수 빼기')
  #   print('3. 두수 곱하기')
  #   print('4. 두수 나누기')
  #   print('-' * 50)
  #   choice = int(input('원하는 번호를 입력하세요. >> '))
  #   if choice == 1: print(f'결과값 : {num1 + num2}')
  #   elif choice == 2: print(f'결과값 : {num1 - num2}')
  #   elif choice == 3: print(f'결과값 : {num1 * num2}')
  #   else: print(f'결과값 : {num1 / num2}')
    

  # i, j = 1, 1
  # while i < 10:
  #   while j < 10:
  #     if j % 2 == 0:
  #       j += 1
  #       continue
  #     print(i, j)
  #     j += 1
  #   j = 1
  #   i += 1

  # i, j = 0, 0
  # while i < 10:
  #   print('번호 1번 : ', i)
  #   while j < 10:
  #     if j == 5: break
  #     print('번호 2번 : ', j)
  #     j += i


  # 입력한 숫자를 계속 더하는 프로그램을 만드시오.
  # i = 0
  # while True:
  #   num = int(input('숫자를 입력하세요. 0은 종료 입니다. '))
  #   if not num:
  #     print('종료 되었습니다.')
  #     break
  #   i += num
  #   print(f'결과 : {i}')
  
  # i = 0
  # while True: # 무한반복
  #   print(i)
  
  # 구구단을 출력하시오.
  # i = 1
  # while i < 10:
  #   j = 1
  #   while j < 10:
  #     print(f'{i} * {j} = {i * j}')
  #     j += 1
  #   i += 1
  
  # for i in range(1, 10):
  #   for j in range(1, 10):
  #     print(f'{i} * {j} = {i * j}')

  # i = 0
  # while i < 10:
  #   print(i)
  #   i += 1

  # for i in range(10):
  #   print(i)