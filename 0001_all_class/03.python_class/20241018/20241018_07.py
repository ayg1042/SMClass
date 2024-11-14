# a = [1, 2, 3]
# print(*a)

# s_title = ['번호','이름','국어','영어','수학','합계','평균','등수'] #전역변수
# print(*s_title, sep='\t')

class student:
  # 인스턴스 변수 - 객체선언은 개별 변수로 작동
  count = 0 # 클래스 변수 - 모든 객체가 동일한 변수를 사용

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
  
  # == : 호출되는 함수
  # self : 자신 객체
  # value : 비교할 객체
  def __eq__(self, value):
    return self.total == value.total
  def __ne__(self, value):
    return self.total != value.total 
  def __gt__(self, value):
    return self.total > value.total 
  def __ge__(self, value):
    return self.total >= value.total 
  def __lt__(self, value):
    return self.total < value.total 
  def __le__(self, value):
    return self.total <= value.total


s1 = student('홍길동', 80, 100, 100)
s2 = student('유관순', 90, 100 ,90)

if s1 == s2:
  print('12')
else:
  print('34')