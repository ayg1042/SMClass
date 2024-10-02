import random as rd




if __name__=='__main__':
  # 1 ~ 100까지의 랜덤숫자를 생성
  # 입력한 숫자가 랜덤숫자 보다 크면 입력한 숫자가 큽니다.
  # 입력한 숫자가 랜덤 숫자보다 작으면 입력한 숫자가 작습니다.
  # 10번 도전
  # 정답입니다. 프로그램 종료 하시오.
  r_num = rd.randint(1, 100)
  i = 0
  while i < 10:
    num = int(input(f'{i + 1}회 숫자를 입력하세요. '))
    if num < r_num: print('숫자가 작습니다.')
    elif num > r_num: print('숫자가 큼니다.')
    else:
      print('정답입니다.')
      break
    i += 1
  print(f'정답은 [{r_num}] 입니다.')

  # for i in range(10):
  #   num = int(input(f'{i + 1}회 숫자를 입력하세요. '))
  #   if num < r_num: print('숫자가 작습니다.')
  #   elif num > r_num: print('숫자가 큼니다.')
  #   else:
  #     print('정답입니다.')
  #     break
  # print(f'정답은 [{r_num}] 입니다.')