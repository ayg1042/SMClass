import random as rd


if __name__ == "__main__":
  r_num = rd.randint(1, 100)
  get = True
  for i in range(10):
    num = int(input(f'{i + 1}번째 숫자를 입력하세요. '))
    if r_num == num:
      print("정답입니다.")
      get = False
      break
    elif r_num > num: print('숫자가 작습니다.')
    else: print('숫자가 큼니다.')
  if get:
    print(f'실패 하셨습니다.\n정답은 [{r_num}] 입니다.')