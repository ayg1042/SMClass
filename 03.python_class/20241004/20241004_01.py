





if __name__=="__main__":
  students = [
    [1,'홍길동',100,90,99],
    [2,'유관순',100,100,99],
    [3,'이순신',100,100,99],
    [4,'강감찬',100,90,99],
    [5,'김구',90,90,99]
  ]
  # 합계, 평균 추가해서 전체를 출력하시오.
  # 1 홍길동 100 90 99 289 92.00
  for i in students:
    i.append(i[2] + i[3] + i[4])
    i.append(round(i[5]/3, 2))
    print(f'{i[0]}\t {i[1]}\t {i[2]}\t {i[3]}\t {i[4]}\t {i[5]}\t {i[6]}')
    print('{}\t {}\t {}\t {}\t {}\t {}\t {:.2f}'.format(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))