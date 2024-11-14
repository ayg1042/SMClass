

if __name__=="__main__":
  stu_title = ['번호', '이름', '국어', '영어', '수학', '과학', '합계', '평균']
  stu_datas = [
    [1, '홍길동', 100, 100, 100, 99],
    [2, '유관순', 100, 100, 100, 99],
    [3, '이순신', 100, 99, 98, 99],
    [4, '김구', 80, 100, 90, 99],
    [5, '김유신', 80, 100, 90, 99]
  ]

  # for i in stu_title:
  #   print("{}".format(i), end='\t')
  # print()
  # print('-' * 60)
  # for i in stu_datas:
  #   total = i[2] + i[3] + i[4] + i[5]
  #   avg = total/4
  #   print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t".format(i[0], i[1], i[2], i[3], i[4], i[5], total, avg))

  # list 추가 append(값), insert(위치, 값)
  a_list = [1, 2, 3, 4]
  a_list.append(5)
  print(a_list)
  a_list.insert(0, 50)
  print(a_list)

  # list 삭제 del, remove(데이터 값)
  del a_list[0]
  print(a_list)
  a_list.remove(5)
  print(a_list)