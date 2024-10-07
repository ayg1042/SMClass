








if __name__ =="__main__":
  
  a = [i for i in range(1, 10)]
  print(a)

  b = []
  c = []
  for i in range(1, 26):
    if i % 5 != 0:
      c.append(i)
    else:
      c.append(i)
      b.append(c)
      c = []
  print(b)
  # for 문을 사용해서, 2차원 리스트에 추가하시오.
  # a = []
  # count = 1
  # for i in range(0, 3):
  #   b = []
  #   for j in range(0, 3):
  #     b.append(count)
  #     print((3 * i) + j + 1)
  #     count += 1
  #   a.append(b)
  # print(a)
  # [3, 3] 리스트 [1, 2, 3][4, 5, 6][7, 8, 9]
  # a = [
  #   [1, 2, 3],
  #   [4, 5, 6],
  #   [7, 8, 9]
  # ]

  # 1 ~ 9 까지 for문을 사용해서, 1차원 리스트 추가
  # b = []
  # for i in range(1, 10):
  #   b.append(i)

  # print(b)