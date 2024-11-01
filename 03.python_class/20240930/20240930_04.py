




if __name__ == "__main__":

  # name, kor, eng, math, total, avg 출력
  # input으로 입력받아
  # 홍길동, 100, 100, 99 합계, 평균 1줄에 출력하시오.
  name = input('이름 : ')
  kor = int(input('국어 : '))
  eng = int(input('영어 : '))
  math = int(input('수학 : '))
  total = kor + eng + math
  avg = round(total/3, 2)
  print(f'{name}의 점수 합계 : {total}, 평균 : {avg}')
  print('{}의 점수 합계 : {}, 평균 : {}'.format(name, total, avg))



  # 타입변환 int(), float(), str(), bool()
  # a = '100'
  # b = '200'
  # print(int(a) + int(b))
  # c = '3.14'
  # print(float(c))
  # print(int(float(c)))
  # print(str(c))

  # var1 = 100
  # var2 = var1
  # var3 = var2
  # var4 = var3
  # print(var4)

  # v4 = v3 = v2 = v1 = 10
  # print(v4)

  # name = '홍길동'
  # print(type(name))

  # level = '3레벨'
  # print(type(level))

  # n = 3.14
  # print(type(n))

  # num = 100
  # print(type(num))

  # a_bool = True
  # print(type(a_bool))