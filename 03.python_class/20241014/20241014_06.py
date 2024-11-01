import random as rd








if __name__ == "__main__":
  fruit = {
    '바나나': 'banana',
    "오렌지": 'orange',
    '체리': 'cherry',
    '파인애플': 'pineapple',
    '코코넛': 'coconut'
    }
  fName = ['바나나', '오렌지', '체리', '파인애플', '코코넛']

  # rd.shuffle(fName)
  re_fName = rd.sample(fName, 5)

  for i in range(len(fName)):
    print(re_fName[i])
    search = input(f'{re_fName[i]}의 영문을 입력하세요. >> ')
    if fruit[re_fName[i]] == search:
      print('정답입니다. ',fruit[re_fName[i]], search)
    else:
      print('오답입니다. ',fruit[re_fName[i]], search)


  # for i in range(5):
  #   ran = fName[rd.randint(0, 4)]


  # fName에 맞춰 진행
  # print('[ 영단어 맞추기 ]')
  # for key in fName:
  #   search = input(f'{key}의 영문을 입력하세요. >> ')
  #   if fruit[key] == search:
  #     print('정답입니다. ',fruit[key], search)
  #   else:
  #     print('오답입니다. ',fruit[key], search)


  # print('[ 영단어 맞추기 ]')
  # for key in fruit.keys():
  #   search = input(f'{key}의 영문을 입력하세요. >> ')
  #   if fruit[key] == search:
  #     print('정답입니다. ',fruit[key], search)
  #   else:
  #     print('오답입니다. ',fruit[key], search)

  # search = input('바나나의 영문을 입력하세요. >> ')
  # if fruit['바나나'] == search:
  #   print('정답입니다. ',fruit['바나나'], search)
  # else:
  #   print('오답입니다. ',fruit['바나나'], search)


  # 바나나를 입력하면 영어로 출력하세요.
  # while True:
  #   search = input('과일이름을 입력하세요. >> ')
  #   if search in fruit: print('영문으로 : ',fruit[search])
  #   else: print('찾는 단어가 없습니다.')