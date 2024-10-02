





if __name__ == "__main__":
  fruit = []

  while True:
    # rstrip() 앞쪽여백, 뒤쪽여백 제거
    # search = input('과일이름을 입력하세요.(종료 : X) ').rstrip()
    search = input('과일이름을 입력하세요.(종료 : X) ').replace(" ", '')
    if(search == 'x' or search == "X"):
      break
    if search in fruit: print('이미 등록된 과일입니다.\n', fruit)
    else:fruit.append(search)
  print("등록된 과일 : ", fruit)
  # a = 0
  # while True: 무한반복
  # while a < 10:
  #   a += 1
  #   print(a)
  
  # print("프로그램종료")