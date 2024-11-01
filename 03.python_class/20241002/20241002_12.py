import random as rd





if __name__=='__main__':
  # random 숫자 생성
  # 0 <= x <= 1
  print(rd.random())
  # 0 ~ 9
  print(int(rd.random() * 10))
  # 1 ~ 10
  print(int(rd.random() * 10) + 1)

  # 랜덤 int 추출 1 ~ 3 까지 포함 O
  print(rd.randint(1, 3))
  # 랜덤 범위 추출 1 ~ 3 까지 포함 X
  print(rd.randrange(1, 3))

  # 리스트를 활용한 랜덤 추출
  a = [1, 2, 4, 6, 7, 9]
  print(rd.choice(a))
  # 리스트에서 여러개 랜덤 추출 (중복 가능)
  print(rd.choices(a, k=2))
  # 리스트에서 여러개 랜덤 추출 (중복 불가)
  print(rd.sample(a, 2))
