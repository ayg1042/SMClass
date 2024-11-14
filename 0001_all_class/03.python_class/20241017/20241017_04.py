# try - except - else - finally
# Exception
# raise : 강제 예외
# 리스트의 범위 밖 호출 에러 : IndexError
# 입력된 값의 변환 에러 : ValueError


print('프로그램을 시작합니다. ')
print('1')
print('2')
try:
  print('3')
  print('4')
  print('5')
  raise NotImplementedError('프로그램을 구현해야 함') # 프로그램을 구현되어 있지 않을 때
except Exception as e:
  print('e : ', e)
  print('6')
  print('7')
  print('8')
finally:
  print('9')
  print('10')
  print('11')




# list1 = [52, 273, 32, 72, 100]

# try:
#   n_input = int(input('정수를 입력하세요. >> '))
#   print(f'{n_input}번째 리스트의 값 : {list1[n_input]}')
# except ValueError as e:
#   print('값을 잘못입력하셨습니다.', e)
# except IndexError as e:
#   print('번호가 범위를 벗어났습니다.', e)
# except Exception as e: # Excption 가장 마지막에
#   print(type(e))
#   print('e : ', e)
# finally:
#   print('끝')

