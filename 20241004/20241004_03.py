



if __name__=='__main__':
  for i in range(10):
    print(i)
  print('*' * 20)
  
  for i in range(5, 10):
    print(i)
  print('*' * 20)

  a = [1, 2, 3, 4, 5]
  for i in a:
    print(i)
  print('*' * 20)

  b = [3, 5, 6, 8, 9, 6]
  print(len(b))
  print('*' * 20)

  print(b.count(6))

  # 리스트 추가 = append, insert, extend([2, 3])
  # 리스트 삭제 = del, remove, clear

  # 딕셔너리 타입 {key: value}
  dic = {1: '안녕', 2: '하세요', 3: '오늘도', 4: '좋은하루', 'key': '되세요'}
  print(dic)
  print(dic.values)
  for i in dic:
    print(i)

  s = (1, 2, 3, 4)
  print(type(s))