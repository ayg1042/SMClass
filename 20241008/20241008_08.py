








if __name__ == '__main__':

  name = ['홍길동', '유관순', '이순신']
  score = [100, 90, 95]

  n_dic = dict(zip(name, score))
  print(n_dic)
  # a = n_dic # 얕은 복사
  a = n_dic.copy()

  a['홍길동'] = 0
  print(n_dic)
  print(a)

  # 얕은 복자, 깊은복사
  # name = ['홍길동', '유관순', '이순신']
  # score = [100, 90, 95]

  # n = name # 얕은 복사
  # n = name[:] # 깊은 복사
  # n[2] = '김구' # n의 이순신 변경 -> 김구로 변경
  # print(n) 

  # print(name)