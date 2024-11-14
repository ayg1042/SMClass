



if __name__ == "__main__":

  stus = [
    [1, "김김김", 100, 99, 98],
    [2, "수수수", 97, 96, 95],
    [3, "가가가", 94, 93, 92]
  ]
  s = [4, '이이이', 91, 90, 89]
  s.append(s[2] + s[3] + s[4])
  s.append(round(s[5]/3, 2))
  print(s)

  for a, data in enumerate(s):
    print(a, " : ", data)

  # str = "좋은 하루되세요. 많은 행복받으세요. 많은 돈."
  # print(len(str))
  # # 뒤쪽에서 5자리 전까지 출력
  # print(str[-5:])