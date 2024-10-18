# 학생 1명 정보
# 번호, 이름, 국어, 영어, 수학, 합계, 평균, 등수
# 학생클래스 설계도 생성
class Student:
  # 생성자
  def __init__(self, no, name, kor, eng, math):
    self.no = no
    self.name = name
    self.kor = kor
    self.eng = eng
    self.math = math
    self.total = kor + eng + math
    self.avg = self.total/3
    self.rank = 0
  
  def print(self):
    print(f'{self.no}, {self.name}, {self.kor}, {self.eng}, {self.math}, {self.total}, {self.avg}, {self.rank}')

# 전체학생리스트 정보
class Students:
  pass

# 클래스명.변수명 = 값
# 기본생성자
s1 = Student(1, '홍길동', 100, 100, 100)

s1.print()

# s2 = Student()
# s2.no = 2
# s2.name = '유관순'
# s2.kor = 100
# s2.eng = 100
# s2.math = 100
