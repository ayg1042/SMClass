import random as rd


if __name__=="__main__":
  r_num = rd.randint(1, 100)
  # 10번 도전에서 입력한 숫자가 더 크면
  # 작은수를 입력하셔야 합니다.
  # 큰수를 입력하셔야 합니다.
  i = 0
  check = True
  while i < 10:
    num = int(input(f'{i + 1}번째 도전, 숫자를 입력하세요. '))
    if num < r_num: print(f'숫자가 작습니다.')
    elif num > r_num: print(f'숫자가 큼니다.')
    else:
      print('정답입니다.')
      check = False
      break
    i += 1
  if check:
    print(f'실패 했습니다.\n정답은 [{r_num}] 입니다.')