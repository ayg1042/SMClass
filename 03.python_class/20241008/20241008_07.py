import operator








if __name__ == "__main__":

  name = ['홍길동', '유관순', '이순신']
  score = [100, 90, 95]

  # 딕셔너리타입 리스트 생성
  # d_dic = dict(zip(name, score))
  # print(d_dic)

  # 튜플타입 리스트 생성
  # n_list = list(zip(name, score))
  # print(n_list)

  # zip() 함수
  # for i, j in zip(name, score):
  #   n_list.append([i, j])
  #   print(i, j)
  # print(n_list)

  # num_list = []
  # # 1,2,3,4,5 추가

  # # 리스트 내포, 컴프리헨션
  # num_list = [i for i in range(1, 6)]
  # print(num_list)

  # a_list = [i * i for i in range(5)]
  # print(a_list)

  # # 정수형 -> 문자형
  # b_list = [str(i) for i in range(5)]
  # print(b_list)

  # # 문자형 -> 정수형
  # c_list = ['5', '6', '7', '8', '9']
  # cc_list = [int(i) for i in c_list]
  # print(c_list)
  # print(cc_list)

  # d_str = '1, 2, 23, 5, 9'
  # d_sp = [int(i) for i in d_str.split(',')]
  # print(d_sp)

  # score = input('좌표를 입력하세요. (0.0)>> ')
  # sc = [int(i) for i in score.split('.')]
  # print(score)
  # print(sc)

  # students = [
  #   {'no': 1, 'name': "홍길동", 'kor': 100, 'eng': 100, 'math': 99, 'total': 299, 'avg': 99.67, 'rank': 0},
  #   {'no': 2, 'name': "유관순", 'kor': 80, 'eng': 80, 'math': 85, 'total': 245, 'avg': 81.67, 'rank': 0},
  #   {'no': 3, 'name': "이순신", 'kor': 90, 'eng': 90, 'math': 91, 'total': 271, 'avg': 90.33, 'rank': 0},
  #   {'no': 4, 'name': "강감찬", 'kor': 60, 'eng': 65, 'math': 67, 'total': 192, 'avg': 64.00, 'rank': 0},
  #   {'no': 5, 'name': "김구", 'kor': 100, 'eng': 100, 'math': 84, 'total': 284, 'avg': 94.67, 'rank': 0}
  # ]

  # 리스트 딕셔너리 정렬
  # for s in students:
  #   print(s)

  # 안됨
  # print(students)
  # x = sorted(students.items())
  # print('-' * 60)
  # print(x)


  # nameDic = {
  #   '홍길동': 100,
  #   '유관순': 80,
  #   '이순신': 95,
  #   '강감찬': 82,
  #   '김구' : 97
  # }
  # key, value = 모두 가져올 수 있는 것
  # nameDic.items()
  # nameDic = sorted(nameDic.items()) # [0] 번째로 순차정렬
  # nameDic = sorted(nameDic.items(), reverse=True) # [0] 번째로 역순정렬
  # key - [0], value - [1]
  # import operator 해줘야함
  # lambda x:x[0], lambda x:x[1]
  # nameDic = sorted(nameDic.items(), key=operator.itemgetter(1)) # [1] 번째로 순차정렬
  # print('*' * 50)
  # print(nameDic)