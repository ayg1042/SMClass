

if __name__=="__main__":

  stu_title = ['번호', '이름', '국어', '영어', '수학', '과학', '합계', '평균']
  stu_datas = [
    [1, '유관순', 100, 100, 100, 99],
    [2, '이순신', 100, 99, 98, 99],
    [3, '김구', 80, 100, 90, 99]
  ]

  print("                   [ 학생성적 프로그램 ]")
  # print("{}, {}, {}, {}, {}, {}, {}, {}".format(stu_title[0], stu_title[1],
  #   stu_title[2], stu_title[3], stu_title[4], stu_title[5], stu_title[6],
  #   stu_title[7]))
  for s_t in stu_title:
    print("{}".format(s_t), end='\t')
  print()
  print('-' * 60)

  for i in stu_datas:
    total = i[2] + i[3] + i[4] + i[5]
    avg = round(total/4, 2)
    # print(f'번호 : {i[0]}, 이름 : {i[1]}, 국어 : {i[2]}, 영어 : {i[3]}, 수학 : {i[4]}')
    print(f'{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}\t{i[5]}\t{total}\t{avg}\t')

  # avg = round((stu_datas[1][1] + stu_datas[1][2] + stu_datas[1][3] + stu_datas[1][4])/4, 2)
  # print(f'학생이름 : {stu_datas[1][0]}')
  # print(f'평균 : {avg}')

  # stu_data = ['홍길동', 100, 100, 100, 99]
  # print(f"학생이름 : {stu_data[0]}\n국어 : {stu_data[1]}\n영어 : {stu_data[2]}\n수학 : {stu_data[3]}\n과학 : {stu_data[4]}\n합계 : {stu_data[1] + stu_data[2] + stu_data[3] + stu_data[4]}\n평균 : {(stu_data[1] + stu_data[2] + stu_data[3] + stu_data[4]) / 4}")

  # 1번에 2개 두 길이를 입력받아, 삼각형의 넓이, 직사각형의 넓이를 구하시오.
  # a, b = (input('길이1 : ')).split(' ')
  # a, b  = map(int, input('두 숫자 입력 : ').split())

  # print(f'삼각형 넓이 : {(a * b) / 2}')
  # print(f'직사각형 넓이 : {(a + b) * 2}')

  # 원의 넓이 : 반지름 * 반지름 * 3.14
  # 반지름을 입력받아, 원의 넓이를 구하시오.
  # a = int(input("반지름 : "))
  # print(f'원의 넓이 = {a*a*3.14}')

  # 복합대입연산자 +=, -=, //=, **=
  # a = 10
  # a += 5
  # print(a)
  # a = 10
  # a -= 5
  # print(a)
  # a = 10
  # a *= 5
  # print(a)
  # a = 10
  # a /= 5
  # print(a)

  # a, b = 10, 5

  # for i in range(1, 21):
  #   print(i % 10)
  #   print(i / 10)

  # print(2 + 2 - 2 * 2 / 2 * 2)
  # a, b = 5, 3
  # print(f"{a} / {b} = {a / b}")
  # print(f"{a} % {b} = {a % b}")
  # print(f"{a} // {b} = {a // b}")
  # print(f"{a} ** {b} = {a ** b}")
  # print("{} / {}  = {}".format(a, b, a / b))
  # print("{} % {}  = {}".format(a, b, a % b))
  # print("{} // {}  = {}".format(a, b, a // b))
  # print("{} ** {}  = {}".format(a, b, a ** b))