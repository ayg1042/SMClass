




if __name__=="__main__":
  students = [
    [1, '홍길동', 100, 90, 99],
    [2, '유관순', 200, 90, 99],
    [3, '이순신', 100, 90, 99],
    [4, '강감찬', 100, 90, 99],
    [5, '김구', 100, 90, 99]
  ]

  # 합계, 평균 추가
  for i in students:
    i.append(i[2] + i[3] + i[4])
    i.append(round(i[5]/3, 2))

  name = input('찾고자하는 학생이름을 입력하세요.')
  cnt = 0
  for i in students:
    # 찾는 학생이 있으면 있습니다.
    # 없으면 찾는 학생 이름이 없습니다.
    if name in i:
      cnt += 1

  if cnt: print('해당 이름의 학생이 있습니다.')
  else: print('해당 이름의 학생은 없습니다.')