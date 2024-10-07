import random as rd








if __name__=="__main__":
  # 25개 1차원 리스트
  # 25개 중 1을 5개 나머지는 0으로 입력해서 출력하시오.
  
  a_list = []
  for i in range(25):
    if i < 5:
      a_list.append(1)
    else:
      a_list.append(0)
  rd.shuffle(a_list)
  # print(a_list)

  # [5, 5] 2차원리스트에 a_list의 값을 입력한후 출력하시오.
  b_list = []
  for i in range(0, len(a_list), 5):
    b_list.append(a_list[i:i+5])

  # print(b_list)
  while True:
    print('\t0\t1\t2\t3\t4\t')
    print("-" * 50)
    for i in range(5):
      print(i, end='\t')
      for j in range(5):
        print(b_list[i][j], end='\t')
      print()
    a, b = map(int, input('좌표 입력하세요. (0, 1) >> ').split(','))
    print(f'{a}, {b}좌표의 값은 : {b_list[a][b]}')


  # a_list = [0] * 20 + [1] * 5
  # print(a_list)

  # a_list = [0 for i in range(20)]
  # for i in range(5):
  #   a_list.append(1)
  # print(a_list)