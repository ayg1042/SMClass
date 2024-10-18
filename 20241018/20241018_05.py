class Circle:
  
  def __init__(self, length):
    self._length = length # 내부클래스만 변수에 접근해서 수정이 가능함
    self.__test = 0
  
  def test(self):
    print(self.__test)
  
  def set_test(self, value):
    self.__test = value
  
c1 = Circle(10)
print(c1._length)
# print(c1.__test)
# print(Circle__test)

c1.__test = 1 # __test 라는 변수가 만들어짐
print(c1.__test) # 출력값 1 # 변수값의 출력
c1.test() # 출력값 0 # private 값 출력
c1.set_test(10) # 10 # private 값 변경
c1.test() # private 값 출력