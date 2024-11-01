





if __name__=="__main__":
  a = [1, 2, 3, 4, 5]
  c = a # 얕은 복사
  b = a.copy() # 깊은 복사
  b[0] = 2
  print(a)
  print(b)

  # 데이터 값이 1개일때
  # num = 10
  # num2 = num
  # num2 = 20
