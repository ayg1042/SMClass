import random as rd








if __name__=="__main__":
  lotto = [0] * 6 + [1] * 3
  rd.shuffle(lotto)
  a_list = []
  for i in range(0, len(lotto), 3):
    a_list.append(lotto[i:i+3])

  lotto = ['로또'] * 9
  b_list = []
  for i in range(0, len(lotto), 3):
    b_list.append(lotto[i:i+3])
  
  while True:
    print('\t0\t1\t2')
    print('-' * 30)
    for i in range(len(a_list)):
      print(i,end="\t")
      for j in range(len(a_list[0])):
        print(b_list[i][j], end="\t")
      print('')
    money = int(input('금액 입력 : '))
    if not money: break
    point_x, point_y = map(int, input('좌표를 입력하세요. (0, 0) >> ').split(','))
    if a_list[point_x][point_y]:
      print(f'당첨 입니다. {money * 10:,d}')
      b_list[point_x][point_y] = "당첨"
    else:
      print('꽝 입니다.')
      b_list[point_x][point_y] = "꽝"
