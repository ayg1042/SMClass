





def calc(hh):
  global h
  hh = h + 100
  return hh


if __name__ == "__main__":
  # 함수 - 매개변수 (일반변수, 복합변수)
  h = 20
  h = calc(h)
  print(h)