



if __name__=="__main__":

  all_list = [
  [1, '홍길동', 100, 90, 99],
  [2, '유관순', 200, 90, 99],
  [3, '이순신', 100, 90, 99],
  [4, '강감찬', 100, 90, 99],
  [5, '김구', 100, 90, 99]
  ]

  # 이름을 입력받아 같은 이름이 있으면
  # 데이터 삭제, 없으면 없습니다 출력
  name = input('이름을 출력하세요. ')

  # T = True
  # for i in all_list:
  #   if name == i[1]:
  #     all_list.remove(i)
  #     T = False
  # if T: print('이름이 없습니다.')
  # else: print('삭제되었습니다.')
  # print(all_list)

  count = 0
  for i in all_list:
    if name == i[1]:
      all_list.remove(i)
      count += 1
      
  if count: print('삭제되었습니다.')
  else: print('이름이 없습니다.')
  print(all_list)

  # a = [3, '이순신', 100]
  # # all_list.remove(a)
  # print(all_list)

  # for i in all_list:
  #   if i[1] == '유관순':
  #     all_list.remove(i)
  # print(all_list)

  # test = [
  #   [1, '홍길동', 100],
  #   [1, '홍길동', 200],
  #   [3, '홍길동', 100]
  # ]
  # a = [3, '홍길동', 100]
  
  # for i, d in enumerate(test):
  #   print(i, d)
  #   if d[1] == a[1]:
  #     print(d)
  #     del test[i]
  # print(test)


  # a = [1, '홍길동', 100]
  # b = [1, '홍길동', 200]
  # c = [1, '홍길동', 100]


  # aArr = [2, 3, 4, 6, 7, 8, 9, 10]
  # # 50, 100을 추가하시오.
  # aArr.append(50)
  # aArr.append(100)
  # print(aArr)

  # # 2번자리에 30을 추가하시오
  # aArr.insert(2, 30)
  # print(aArr)

  # # 숫자 6을 삭제하시오.
  # aArr.remove(6)
  # print(aArr)

  # # index 0, 3 데이터를 삭제하시오
  # del aArr[0]
  # del aArr[3]
  # print(aArr)

