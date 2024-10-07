import random as rd








if __name__ == "__main__":

  lotto = [0] * 6 + [1] * 3
  rd.shuffle(lotto)

  a_list = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 0]
  ]

  count = 0
  for i in range(3):
    for j in range(3):
      a_list[i][j] = lotto[count]
      count += 1

  # print(a_list)

  aa_list = [
    ['로또', '로또', '로또'],
    ['로또', '로또', '로또'],
    ['로또', '로또', '로또']
  ]

  # print(a_list)
  while True:
    point = int(input('금액 : '))
    print('         [i, j] 좌표')
    print('\t0\t1\t2\t')
    print('-' * 30)
    for i in range(len(aa_list)):
      print(i, '|', end='\t')
      for j in range(len(aa_list[0])):
        print(aa_list[i][j], end='\t')
      print()
    code = input('좌표를 입력하세요.(0.0) >> ').split('.')
    print(f'code{code[0]},{code[1]} 입력된 좌표값 : ',a_list[int(code[0])][int(code[1])])
    if a_list[int(code[0])][int(code[1])]:
      print(f"당첨 : {point * 10 :,d}")
      aa_list[int(code[0])][int(code[1])] = '당첨'
    else:
      print(f'꽝 : {point}')
      aa_list[int(code[0])][int(code[1])] = '꽝'
    