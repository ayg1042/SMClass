class student:
  # 인스턴스 변수 - 객체선언은 개별 변수로 작동
  count = 0 # 클래스 변수 - 모든 객체가 동일한 변수를 사용
  students = []
  s_title = ['번호','이름','국어','영어','수학','합계','평균','등수'] #전역변수

  # 클래스 함수
  # 클래스 함수 표시
  @classmethod
  def stu_print(cls):
    print('[ 학생성적 출력 ]')
    print(*cls.s_title, sep='\t')
    print('-' * 60)
    for i in cls.students:
      print(str(i))

  def __init__(self, name, kor, eng, math):
    student.count += 1
    self.no = student.count
    self.name = name
    self.kor = kor
    self.eng = eng
    self.math = math
    self.total = kor + eng+ math
    self.avg = self.total/3
    self.rank = 0
    # 클래스 리스트에 추가
    student.students.append(self)


  def __str__(self):
    return f'{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg:.2f}\t{self.rank}'
  
  def print(self):
    return {'no':self.no,'name':self.name,'kor':self.kor,'eng':self.math,'math':self.math,'total':self.total,'avg':self.avg,'rank':self.rank}


s_t = ["no", "name", "kor", "eng", "math", "total", "avg", "rank"]
s_title = ['번호','이름','국어','영어','수학','합계','평균','등수']

students = []
# s1 = student('홍길동', 100, 100, 100)
# print(s1.no)
# print(s1)

# s2 = student('유관순', 100, 100 ,100)
# print(s2.no)
# print(s1.no)
# print(s1.count)

# students.append(s1)
# students.append(s2)

while True:
  print('[ 학생성적 프로그램 ]')
  print('1. 학생성적입력')
  print('2. 학생성적출력')
  choice = input('원하는 번호를 입력하세요. >> ')
  if choice == '0': break
  elif choice == '1':
    print('[ 학생성적 입력 ]')
    name = input('이름을 입력하세요. >> ')
    score = []
    for i in range(3):
      score.append(int(input(f'{s_title[i + 2]} 점수를 입력하세요. >> ')))
    # s1 = student(name, score[0], score[1], score[2])
    # s1 =  student(name, *score)# 위와 같은 코드
    s1 = student(name, *score)


    # 클래스 변수 접근 방법
    for s in student.students:
      print(s)

    # students.append(student(name, *score))
    # print(s1.students[0])
  elif choice == '2':
    # print('[ 학생성적 출력 ]')
    # print(*s_title, sep='\t')
    # print('-' * 60)
    student.stu_print()
  elif choice == '3':
    s1 = student('홍길동', 100, 100, 90)
    s2 = student('유관순', 90, 100 ,90)

    # 인스턴스변수 참조변수.변수명, 참조변수명.함수명
    # 클래스변수 클래스명.변수명, 클래스명.함수명
    # 