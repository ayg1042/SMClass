import random as rd








if __name__ == '__main__':
  # 25개 1차원 리스트 - 1 ~ 25 입력 후 랜덤으로 다시 출력
  # [5, 5] 2차원 리스트 입력 후 출력하시오.
  a = []
  for i in range(25):
    a.append(i + 1)
  rd.shuffle(a)
  
  a_list = []
  for i in range(5):
    b = []
    for j in range(5):
      b.append(a[5 * i + j])
    a_list.append(b)
  print(a_list)

  while True:
    print('\t0\t1\t2\t3\t4')
    print('-' * 60)
    for i in range(5):
      print(i, '|',end='\t')
      for j in range(5):
        print(a_list[i][j], end='\t')
      print()
    # re = input('좌표를 입력하세요. (0.0) >> ')
    # result = re.split('.')
    # print(f'좌표 값 : {a_list[int(result[0])][int(result[1])]}')

    re = int(input('숫자를 입력하세요 1~25 >> '))
    if re < 0 or re > 25:
      continue
    for i in range(len(a_list)):
      for j in range(len(a_list[0])):
        if re == a_list[i][j]:
          print(f'{re}의 좌표값은 [{i}, {j}] 입니다.')
          a_list[i][j] = 0
        
  for i in a_list:
    for j in i:
      print(j, end='\t')
    print()