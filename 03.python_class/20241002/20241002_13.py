import random as rd



if __name__ == "__main__":
  aArr = []

  while len(aArr) < 10:
    num = int(rd.random() * 10)
    if num in aArr:
      continue
    aArr.append(num)
  print(aArr)
  # 0 ~ 9까지 랜덤숫자를 추출해서 10번 추가하세요
  # for i in range(10):
  #   aArr.append(int(rd.random() * 10))
  # print(aArr)