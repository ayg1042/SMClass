






def num_sum(st, end):
  sum = 0
  for i in range(st, end + 1):
    sum += i
  print('합계 : ',sum)


if __name__=='__main__':
  # 1~10 까지 합계를 출력하시오.
  num_sum(1, 10)

  # 1~100 까지 합계를 출력하시오
  num_sum(1, 100)

  # 2~50 까지 합계를 출력하시오.
  num_sum(2, 50)

  # 100 ~ 1000까지 합계를 출력하시오.
  num_sum(100, 1000)

  # 두수를 입력받아, 그 사이의 숫자 합을 구하시오.
  # num1, num2
  # 함수를 사용해서 출력하시오.
  # num1, num2 = map(int, input('숫자를 입력하세요. (1,2) >> ').split(','))
  # num_sum(num1, num2)

  # # 1, 10까지의 합과 1, 100까지의 합의 총합을 출력하시오.
  # def num_sum(st, end):
  #   num  = 0
  #   for i in range(st, end + 1):
  #     num += i
  #   return num
  # print(num_sum(1, 10) + num_sum(1, 100))

  # # 2 ~ 50, 3 ~ 7, 5 ~ 50합을 모두 더해서 출력하시오.
  # total = num_sum(2, 50) + num_sum(3, 7) + num_sum(1, 100)
  # print(f'합계 : {total:,d}')
  
  
  # def plus(n1, n2):
  #   result = n1 + n2
  #   return result
  # print(plus(1, 2))
  # print(plus(55, 45))
  
  # 두수를 입력받아 더하기를 출력하시오.
  def plus(n1, n2):
    return n1 + n2
  print(plus(int(input('숫자를 입력하세요. >> ')), int(input('숫자를 입력하세요. >> '))))