import random as rd








if __name__=='__main__':
  print(int(rd.random() * 25) + 1)
  print(rd.randint(1, 25))
  # 1, 25까지 랜덤숫자를 입력, 중복은 제거하고 출력하시오.
  # 25번 반복해서
  a_list = []
  b_list = []
  c_list = []

  for i in range(25):
    c_list.append(i + 1)
  d_list = rd.sample(c_list, 25)
  d_list = rd.choices(c_list, k=25) # 중복가능
  print(d_list)

  for i in range(25):
    num = rd.randint(1, 25)
    if num not in b_list:
      b_list.append(num)
  print(b_list)

  while len(a_list) < 25:
    num = rd.randint(1, 25)
    if num not in a_list:
      a_list.append(num)
  print(a_list)






  # # 1차원 리스트 - 25개
  # a_list = []
  # for i in range(25):
  #   a_list.append(i + 1)

  # # 1차원리스트 -> 2차원리스트
  # # 0~25까지 5식 증가
  # b_list = []
  # for i in range(0, len(a_list), 5):
  #   b_list.append(a_list[i:i+5])
  # print(b_list)

  # 1차원리스트 -> 2차원리스트 변경
  # b_list = []
  # for i in range(5):
  #   a = []
  #   for j in range(5):
  #     a.append(5 * i + (j + 1))
  
  # a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  # b = []
  # for i in range(9):
  #   print(3 * (i % 3) + (1 // 3))