






# def cale(num1, num2):
#   for i in range(len(num1)):
#     print('-' * 60)
#     print(f'두수 더하기 : {num1[i] + num2[i]}')
#     print(f'두수 빼기 : {num1[i] - num2[i]}')
#     print(f'두수 나누기 : {num1[i] / num2[i]}')
#     print(f'두수 곱하기 : {num1[i] * num2[i]}')
#     print('-' * 60)

# def cale2(a, b):
#   print('-' * 60)
#   print(f'두수 더하기 : {a + b}')
#   print(f'두수 빼기 : {a - b}')
#   print(f'두수 나누기 : {a / b}')
#   print(f'두수 곱하기 : {a * b}')
#   print('-' * 60)

# def cale3(num):
#   print('-' * 60)
#   print(f'두수 더하기 : {int(num[0]) + int(num[1])}')
#   print(f'두수 빼기 : {int(num[0]) - int(num[1])}')
#   print(f'두수 나누기 : {int(num[0]) / int(num[1])}')
#   print(f'두수 곱하기 : {int(num[0]) * int(num[1])}')
#   print('-' * 60)

# def cale4(num):
#   print('-' * 60)
#   print(f'두수 더하기 : {int(num[0]) + int(num[1]) + int(num[2])}')
#   print(f'두수 빼기 : {int(num[0]) - int(num[1]) - int(num[2])}')
#   print(f'두수 나누기 : {int(num[0]) / int(num[1]) / int(num[2])}')
#   print(f'두수 곱하기 : {int(num[0]) * int(num[1]) * int(num[2])}')
#   print('-' * 60)

# def cale5(num):
#   if len(num) == 3:
#     print('-' * 60)
#     print(f'세수 더하기 : {int(num[0]) + int(num[1]) + int(num[2])}')
#     print(f'세수 빼기 : {int(num[0]) - int(num[1]) - int(num[2])}')
#     print(f'세수 나누기 : {int(num[0]) / int(num[1]) / int(num[2])}')
#     print(f'세수 곱하기 : {int(num[0]) * int(num[1]) * int(num[2])}')
#     print('-' * 60)
#   elif len(num) == 2:
#     print('-' * 60)
#     print(f'두수 더하기 : {int(num[0]) + int(num[1])}')
#     print(f'두수 빼기 : {int(num[0]) - int(num[1])}')
#     print(f'두수 나누기 : {int(num[0]) / int(num[1])}')
#     print(f'두수 곱하기 : {int(num[0]) * int(num[1])}')
#     print('-' * 60)

# def cale6(num):
#   s1 = 0
#   s2 = 0
#   s3 = 1
#   s4 = 1
#   for i in num:
#     s1 += i
#     s2 -= i
#     s3 *= i
#     s4 /= i
#   print('더하기 = ', s1)
#   print('빼기 = ', s2)
#   print('곱하기 = ', s3)
#   print('나누기 = ', s4)

# 가변매개변수
# def calc7(*n):
#   print(n)

#키워드 매개변수
# def calc(n1 = 10, n2 = 20):
#   print(n1, n2)

# def calc(v1, v2):
#   global sum
#   for i in (v1, v2+1):
#     sum += i

# def calc(n1, n2):
#   s1 = n1 + n2
#   s2 = n1 - n2
#   s3 = n1 * n2
#   s4 = n1 / n2
#   return [s1, s2, s3, s4]

# def add(hh):
#   hh = hh + 100

# def add(j):
#   for i in range(len(j)):
#     j[i] += 100

def calc():
  global sum
  sum = 100

if __name__ == "__main__":

  sum = 10
  print(sum)
  calc()
  print(sum)
  # hong = [1, 2, 3, 4, 5]
  # print(hong)
  # add(hong)
  # print(hong)

  # kim = []
  # kin = hong
  # kin[0] = 100
  # print(hong[0])
  # s1, s2, s3, s4 = calc(10, 5)
  # print(calc(11, 6))
  # print(s1, s2, s3, s4)

  # print(1, 2, 3, sep='$', end='\t')

  # calc(n2 = 2)
  # calc(2)
  # calc()

  # numList = input('숫자 3개를 입력하세요. (12,1,2)>> ').split(',')
  # numIntList = [int(i) for i in numList]

  # 3개의 숫자를 입력받아 숫자를 계산하시오. 12, 5, 3
  # numList = input('숫자 3개를 입력하세요. (12,1,2)>> ').split(',')
  # cale5(numList)

  # num1 = input('숫자를 입력하세요. (1,2)>> ').split(',')
  # cale3(num1)

  # num1 = int(input('숫자를 입력하세요. >> '))
  # num2 = int(input('숫자를 입력하세요. >> '))
  # cale2(num1, num2)

  # num = [10, 20 ,30]
  # num2 = [5, 7, 3]
  # # cale(num, num2)
  # for i in range(len(num)):
  #   cale2(num[i], num2[i])

  # for i in range(len(num)):
  #   print('-' * 60)
  #   print(f'두수 더하기 : {num[i] + num2[i]}')
  #   print(f'두수 빼기 : {num[i] - num2[i]}')
  #   print(f'두수 나누기 : {num[i] / num2[i]}')
  #   print(f'두수 곱하기 : {num[i] * num2[i]}')
  #   print('-' * 60)
 