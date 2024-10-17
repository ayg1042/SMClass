# try - except
# try - except = else
# try - except - else - finally

numbers = [52, 273, 32, 103, 90, 10, 275, 1, 2, 1, 2, 12]
try:
  print(numbers.index(52))
  print(numbers.index(1))
  print(numbers.index(3))
except Exception as e:
  print('찾는 번호가 없습니다.', e)




# print('파일 오픈')
# try:
#   print(10)
#   print(10/0)
# except:
#   print(2) # error 발생 시
# else:
#   print(3) # error 미 발생 시
# finally:
#   print(4) # 무조건

# f = open('20241017/a.txt', 'w', encoding='utf-8')
# f.write('안녕하세요.')
# f.write('')
# f.write({'1': 1})
# f.close()



# try:
#   print('1')
#   print('2')
#   print(dfdf)
#   print('4')
#   print('5')
# except:
#   print('6')
#   print('7')

# list_a = [1, 2, 3, 4, 5, '홍길동']
# list_b = []
# try:
#   for a in list_a:
#     list_b.append(a**2)
#   print(list_b)
# except:
#   pass
# print(list_b)


# n_str = input('반지름을 입력하세요 >> ')

# if n_str.isdigit():
#   num = int(n_str)
#   print('원 넓이 : ', (num ** 2) * 3.14)
#   print('원 둘레 : ', num * 2 * 3.14)
# else:
#   print('정수가 아닙니다.')

# try:
#   num = int(n_str)
#   print('원 넓이 : ', (num ** 2) * 3.14)
#   print('원 둘레 : ', num * 2 * 3.14)
# except Exception as e:
#   print(e)
#   print('정수가 아닙니다.')

# print('프로그램 시작')





# try:
#   # print('프로그램 시작) # 구문 오류 - 프로그램 실행 전
#   print(list_a) # 런타임 오류 - 프로그램 실행 중
# except:
#   print('에러 발생')

# print('프로그램 종료')