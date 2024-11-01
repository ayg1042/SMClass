








if __name__ == '__main__':
  dic = {1: '안녕', 2: '하세요', '이름': '홍길동'}
  dic['math'] = 90 # 없는 키를 입력하면 추가됨
  dic['kor'] = 50 # key값이 다르면 다르다고 인식
  del dic['kor']
  print(dic)
  print(dic.get('이름'))
  print(dic.get('없는거'))
  print(dic.keys()) # class 객체 타입 -> index값이 없다
  print(list(dic.keys()))
  print(dic.values())
  print(list(dic.values()))
  print(dic.items())
  print(list(dic.items()))

  for key, val in dic.items():
    print(key, val)
  
  if not dic.get('평균'):
    dic['평균'] = 99.0
  print(dic)


  # 튜플 - 수정안됨