import random as rd








if __name__=="__main__":
  # 1 ~ 25까지 랜덤의 숫자 25개를 중복없이 추출
  # [5, 5] 2차원 리스트에 입력해서 출력하시오.
  
  a_list = []
  b_list = []
  while len(a_list) < 25:
    num = rd.randint(1, 25)
    if num not in a_list:
      a_list.append(num)
  a = []
  for i in a_list:
    a.append(i)
    if len(a) % 5 == 0:
      b_list.append(a)
      a = []

  print(b_list)
  print(a_list)
  rd.shuffle(a_list)
  print(a_list)
  for i in range(0, len(a_list), 5):
    b_list.append(a_list[i: i+5])
  
  while True:
    print('\t0\t1\t2\t3\t4')
    print("-" * 50)
    for i in range(5):
      print(i, end='\t')
      for j in range(5):
        print(b_list[i][j], end='\t')
      print()
    # a, b = map(int, input('좌표를 입력하세요. (0, 1) >> ').split(','))
    input2 = input('좌표를 입력하세요. (0, 1) >> ').split(',')
    # print(f'{a}, {b}좌표의 값 : {b_list[a][b]}')
    print(f'{input2[0]}, {input2[1]}좌표의 값 : {b_list[int(input2[0])][int(input2[1])]}')
