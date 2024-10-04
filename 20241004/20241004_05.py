



if __name__=='__main__':
  # 000
  # 001
  # 999
  for i in range(10):
    for j in range(10):
      for k in range(10):
        print(i,j,k)
  
  for i in range(1000):
    print('{0:0>3}'.format(i))


  # 구구단 입력한 단까지를 출력하시오 3 -> 1, 2, 3단
  # num = int(input('숫자를 입력하세요. '))
  # for i in range(1, num + 1):
  #   for j in range(1, 10):
  #     print(f'{i} * {j} = {i * j}')
  #   print('*' * 30)