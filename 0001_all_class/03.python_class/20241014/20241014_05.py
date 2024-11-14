






# def gugudan(n1, n2):
#   for i in range(n1, n2 + 1):
#     for j in range(1, 10):
#       print(f'{i} * {j} = {i * j}')

# def gugudan(n):
#   for i in range(2, n + 1):
#     for j in range(1, 10):
#       print(f'{i} * {j} = {i * j}')

if __name__ == '__main__':

  subName = ['국어', '영어', '수학']
  score = {'국어': 100, "영어": 95, '수학': 80}
  print(score)
  print(score['국어'])
  print(subName[0])
  print(score[subName[0]])
  for i in subName:
    print(i, ' : ', score[i])
  # for i, j in score.items():
  #   print(i, ' : ', j)


  # nArr = [9, 5, 7]
  # # 2 ~ 9, 2 ~ 5, 2 ~ 7
  # for i in nArr:
  #   gugudan(i)



  # # 구구단을 출력하시오.
  # # 2 ~ 5
  # print('-' * 50)
  # gugudan(2, 5)
  # print('-' * 50)
  # # for i in range(2, 6):
  # #   for j in range(1, 10):
  # #     print(f'{i} * {j} = {i * j}')

  # # 3 ~ 9
  # print('-' * 50)
  # gugudan(3, 9)
  # print('-' * 50)
  # # for i in range(3, 10):
  # #     for j in range(1, 10):
  # #       print(f'{i} * {j} = {i * j}')
  
  # # 5 ~ 8
  # print('-' * 50)
  # gugudan(5, 8)
  # print('-' * 50)
  # # for i in range(5, 9):
  # #   for j in range(1, 10):
  # #     print(f'{i} * {j} = {i * j}')
  
