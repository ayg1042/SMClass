subject = ['국어', '영어', '수학', '과학', '역사']
score = []

while True:
  print('1. 과목추가')
  print('0. 종료')
  choice = input('번호 선택 : ')
  if choice == '0': break


sum = 0
for i in range(5):
  score.append(int(input('점수를 입력하세요. >> ')))
  sum += score[i]
print(sum)

# num1 = int(input('점수 '))
# num2 = int(input('점수 '))
# num3 = int(input('점수 '))



# a = 10
# b = 20
# c = 30
# # 함수를 사용해서, a + b + c의 합 a에 저장해서 출력하시오.
# def add(a, b, c):
#   return a + b + c
# a = add(a, b, c)





# a = 10
# def func():
#   print(a)


# def output(subject):
#   print(' 과목 ')
#   print('-' * 60)
#   for s in subject:
#     print(s)

# subject = ['국어', '영어']
# while True:
#   print(' [ 과목 생성 프로그램 ] ')
#   s_input = input('원하는 과목을 입력하세요. >> ')
#   if s_input == '0': break
#   subject.append(s_input)
#   output(subject)