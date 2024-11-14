








if __name__ == '__main__':
  def calc(n1, n2, op):
    if op == '+':
      return n1 + n2
    elif op == '-':
      return n1 - n2
    elif op == '*':
      return n1 * n2
    elif op == '/':
      return n1 / n2
  num1 = int(input('숫자를 입력하세요. >> '))
  num2 = int(input('숫자를 입력하세요. >> '))
  op = input('+, -, *, / 하나를 선택하세요. ')
  print('결과값 : ', calc(num1, num2, op))