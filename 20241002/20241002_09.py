




if __name__ == "__main__":
  fruit = "사과, 배, 딸기, 포도, 배, 사과, 배, 딸기"
  fruits = fruit.split(', ')
  print(fruits)

  for i, j in enumerate(fruits):
    if j == '배': print(i, " ", j)

  # print(fruit.find('배', 0))
  # print(fruit.find("딸기", 6))