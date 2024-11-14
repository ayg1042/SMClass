







if __name__=="__main__":
  stu_title = ['번호', '이름', '국어', '영어', '수학', '과학', '합계', '평균']
  stu_datas = [
    [1, '홍길동', 100, 100, 100, 99],
    [2, '유관순', 100, 100, 100, 99],
    [3, '이순신', 100, 99, 98, 99],
    [4, '김구', 80, 100, 90, 99],
    [5, '김유신', 80, 100, 90, 99],
  ]
  stu_datas[0]
  # stu = [1, '홍길동', 100, 100, 100, 99]
  for i in stu_datas:
    i.append(i[2] + i[3] + i[4] + i[5])
    i.append(round((i[2] + i[3] + i[4] + i[5])/4, 2))

  j = []
  min = 0
  max = 0
  for i in stu_datas:
    print(i[7])
    if i[7] >= max:
      max = i[7]
      j.append(i[0])
  print(j)


  # print(stu_datas)
  # stu.append(stu[2] + stu[3] + stu[4] + stu[5])
  # stu.append(round((stu[2] + stu[3] + stu[4] + stu[5])/4, 2))
  # print(stu)