




if __name__ == "__main__":

  fruit = "사과, 배, 딸기, 포도, 배, 사과, 배, 딸기, 복숭아, 복숭아"
  # print(fruit.find('배'))
  name = input('과일 이름을 입력하세요. ')
  start = 0
  end = len(name)
  for i in range(fruit.count(name)):
    start += fruit[start:].find(name)
    print(name, ' 위치 : ', start)
    end += start
    print(name ,' : ', fruit[start:end])
    start += 1
    # print(fruit[start-1: start])
    # print(fruit[start-1])

    
  # fruit = ['사과', '배', '딸기', '포도', '복숭아', '배', '사과', '배', '딸기']
  # print(fruit.count('배'))
  # print(fruit.count('사과'))
  # 과일이름을 입력받아 있으면 과일이름이 있습니다다. 과일검색개수: 없으면 없습니다.
  # name = input('과일 이름을 입력하세요. ')
  # if name in fruit: print('{}있습니다.\n과일검색개수{}'.format(name, fruit.count(name)))
  # else: print('없습니다.')

  # index, find

  # 글을 입력받아 입력한 과일이 있으면 있어요, 없으면 없어요.
  # fruit = "사과, 배, 딸기, 포도"
  # name = input('과일 이름을 입력하세요. ')
  # if name in fruit: print("{}가 있어요".format(name))
  # else: print('{}가 없어요'.format(name))

  # fruit = ['사과', '배', '딸기', '포도']
  # if '배' in fruit: print("배가 있어요")
  # else: print('배가 없어요')