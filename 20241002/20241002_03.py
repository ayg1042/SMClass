



if __name__ == "__main__":

  # 숫자를 입력받아 98 ~ 100 A+
  num = int(input("숫자를 입력하세요. "))
  if num >= 98 and num <= 100: print('A+')
  elif num >= 94 and num <= 97: print('A')
  elif num >= 90 and num <= 93: print('A-')
  elif num >= 88 and num <= 89: print('B+')
  elif num >= 84 and num <= 87: print('B')
  elif num >= 80 and num <= 83: print('B-')
  elif num >= 78 and num <= 79: print('C+')
  elif num >= 74 and num <= 77: print('C')
  elif num >= 70 and num <= 73: print('C-')
  elif num >= 60: print('D')
  else: print('F')

  # 숫자를 입력받아
  # num = int(input('숫자를 입력하세요. '))
  # if num >= 3 and num <= 5: print('봄')
  # elif num >= 6 and num <= 8: print('여름')
  # elif num >= 9 and num <= 11: print('가을')
  # elif num >= 13 or num <= 0: print('잘못된 숫자 입니다.')
  # else: print('겨울')

  # 입력한 숫자가 10보다 작거나, 100보다 클때 정답, 오탑
  # num = int(input('숫자를 입력하세요. '))
  # if num <= 10 or num >= 100: print('정답')
  # else: print('오답')

  # 입력한 숫자가 1(포함)보다 크고 10보다 작을 때만
  # 정답, 오답
  # num = int(input('숫자를 입력하세요.'))
  # if num >= 1 and num <= 10: print('정답')
  # else: print('오답')

  # 숫자를 입력받아 짝수, 홀수 인지 출력하시오
  # num = int(input('숫자를 입력하세요.'))
  # if num % 2 == 0: print('짝수 입니다.')
  # else: print('홀수 입니다.')