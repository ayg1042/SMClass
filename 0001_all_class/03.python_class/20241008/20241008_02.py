








if __name__=="__main__":
  # 0, 3, 6, 9, 12, 15 ...
  aArr = []
  for i in range(20):
    aArr.append(i*3)
  print(aArr)

  a_list = []
  for i in range(4):
    a = []
    for j in range(5):
      a.append(aArr[5 * i + j])
    a_list.append(a)
  print(a_list)


  # [4, 5] 리스트를 만들꺼임

  # a_list = []
  # for i in range(4):
  #   a = []
  #   for j in range(5):
  #     a.append(5 * 3 * i + (j + 3))
  #   a_list.append(a)
  # print(a_list)

  # for i in a_list:
  #   for j in i:
  #     print(j, end='\t')
  #   print()


  # a_list =[]
  # a = []
  # for i in range(1, 21):
  #   a.append(i)
  #   if len(a) == 5:
  #     a_list.append(a)
  #     a = []
  # print(a_list)
  
  # b_list = []
  # b = []
  # for i in range(0, 60, 3):
  #   b.append(i)
  #   if len(b) == 5:
  #     b_list.append(b)
  #     b = []
  # print(b_list)