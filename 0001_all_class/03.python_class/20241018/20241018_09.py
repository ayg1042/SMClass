# Student클래스 생성 후
# 데이터를 직접 입력을 받아, 클래스 선언후 저장
# 번호-자동부여, 이름, 국어, 영어, 수학, 합계, 평균, 등수
# 클래스 전체 출력
# 클래스 수정

# [ 학생성적 프로그램 ]
# 1. 학생성적입력
# 2. 학생성적출력
# 3. 학생성적수정

class student:
  __count = 0
  students = []
  s_title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수']
  
  @classmethod
  def cls_mathod(cls):
    print('[성적 출력]')
    print(*cls.s_title, sep='\t')
    print('-' * 60)
    for i in cls.students:
      print(i)

  @classmethod
  def cls_sreach(cls):
    print(' [ 학생정보 검색 ] ')
    name = input('학생 이름을 입력하세요. >> ')
    chx = False
    for i in cls.students:
      if name == i.name:
        chx = True
        sreach = i
    if chx:
      print(f'{name} 학생의 정보 입니다.')
      print(*cls.s_title, sep='\t')
      print('-' * 60)
      print(sreach)
    else: print('없는 학생입니다.')
    return sreach

  @classmethod
  def cls_update(cls, data):
    subjects_point = [data.kor, data.eng, data.math]
    print(' [ 학생정보 수정 ] ')
    for i in range(2, len(cls.s_title) - 3):
      print(f'{i - 1}. {cls.s_title[i]} 점수 수정')
    choice = int(input('수정할 번호를 입력하세요. >> '))
    print(f'기존 {cls.s_title[choice + 1]}점수 입니다 : {subjects_point[choice - 1]}')
    update = int(input('수정할 점수를 입력하세요. >> '))
    subjects_point[choice - 1] = update
    data.kor, data.eng, data.math = subjects_point[0], subjects_point[1], subjects_point[2]
    data.total = sum(subjects_point)
    data.avg = data.total/3
    print('수정이 완료되었습니다.')

  def __init__(self, name, kor, eng, math):
    student.__count += 1
    self.no = self.__count
    self.name = name
    self.kor = kor
    self.eng = eng
    self.math = math
    self.total = kor + eng + math
    self.avg = self.total/3
    self.rank = 0
    student.students.append(self)

  def __str__(self):
    return f'{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg:.2f}\t{self.rank}\t'

  def __gt__(self, value):
    return self.total > value.total
  
  def test(self):
    print(self.name)

if __name__ == '__main__':
  s = student('홍길동', 100, 100, 100)
  student('유관순', 100, 100, 99)

  while True:
    print(' [ 학생성적 프로그램 ] ')
    print(' 1. 학생 등록 ')
    print(' 2. 학생 출력 ')
    print(' 3. 학생정보 검색 ')
    print(' 4. 학생정보 수정 ')
    choice = input('번호를 선택하세요.(0. 종료) >> ')
    if choice == '0': break
    elif choice == '1':
      print(' [ 학생 등록 ] ')
      name = input('이름을 입력하세요. >> ')
      score = []
      for i in range(2, len(student.s_title) - 3):
        score.append(int(input(f'{student.s_title[i]} 점수를 입력하세요. >> ')))
      student(name, *score)
    elif choice == '2':
      student.cls_mathod()
    elif choice == '3':
      student.cls_sreach()
    elif choice == '4':
      student.cls_update()