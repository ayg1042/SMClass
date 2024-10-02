



if __name__ == "__main__":
  stus = [
    [1, "김김김", 100, 99, 98],
    [2, "수수수", 97, 96, 95],
    [3, "가가가", 94, 93, 92]
  ]
  for i in stus:
    if i[1] == "수수수":
      print(i[1])

  s = [4, "나나나", 100, 90, 99]
  stus.append(s)

  for index, data in enumerate(stus):
    if data[1] == "김김김":
      del stus[index]
  print(stus)

  for i in stus:
    if i[1] == "김김김":
      stus.remove(i)

  print(stus)