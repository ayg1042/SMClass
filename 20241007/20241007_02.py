








if __name__=="__main__":
  number = [273, 103, 5, 32, 65, 9, 72, 800, 99]
  for i in number:
    if i >= 100: print(i)


  # a_list = [1, 2, 3, 4, 5]
  
  # a_list[2:3] = [7, 6] # 리스트 2개 변경
  # a_list[2:3] = [] # 2개 삭제시
  # del (a_list) # 전체삭제
  # a_list = [] # 전체삭제 None
  # print(a_list)

  # b_list = [50, 100]
  # print(a_list + b_list)
  # print(b_list * 3)

  

  # b_list = a_list # 얕은 복사

  # b_list = a_list[:] # 깊은 복사

  # # 역순
  # b_list = a_list[::-1]
  # print(a_list)
  # print(b_list)
  # a_list[0] = 100
  # print(b_list)
  # for i in a_list:
  #   print(i)
  # # 역순
  # for i in range(len(a_list)):
  #   print(a_list[-(i + 1)])

  # for i in range(1, len(a_list) + 1):
  #   print(a_list[-i])

  
  # # 문자, 정수, 실수, 논리형
  # a_list = [1, 2, 3.0, '안녕', True, False]
  # print(a_list[0])
  # print(a_list[3])
  # print(a_list[-1])


  # a_list = []
  # # 1 ~ 100까지 들어가 있는 리스트를 출력하시오.
  # for i in range(100):
  #   a_list.append(i+1)
  # print(a_list)

  # a_list = []
  # total = 0

  # for i in range(7):
  #   j = int(input(f'{i + 1}번째 숫자를 입력하세요.'))
  #   a_list.append(j)
  #   total += j
  # print(total)


  # a_list = [0, 0, 0, 0, 0, 0]
  # total = 0
  # for i in a_list:
  #   i = int(input(' 숫자를 입력하세요 >> '))
  #   total += i
  # print('합계 : ', total)
  # print(a_list)

  # a, b, c, d, e = 0, 0, 0, 0, 0
  # total = 0

  # a, b, c, d, e의 변수에 숫자를 입력받아 합계를 출력하시오.
