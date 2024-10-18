# 절차적인 형태의 프로그램 구현
# 반지름을 입력받아, 원의 둘레와 넓이를 출력하세요.


class Circle:
  def __init__(self, length):
    self.__length = length # 번수 직접적으로 접근제한

  def get_area(self):
    return 3.14 * self.__length ** 2
  
  def get_circumference(self):
    return 3.14 * 2 * self.__length

num = int(input('반지름 : '))
print(f'넓이 : {3.14 * num * num}')
print(f'둘레 : {3.14 * 2 * num}')