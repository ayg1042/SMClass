

def money_count(money, cut = 50000, point = 2):
  if cut <= 0: return 0
  elif money >= cut:
    print(cut,"원 개수 : ",money//cut)
    money %= cut
    if point == 2:
      money_count(money, cut//5, 1)
    else:
      money_count(money, cut//2)
  elif money < cut:
    if point == 2:
      money_count(money, cut//5, 1)
    else:
      money_count(money, cut//2)
  elif money < 10:
    return 0
  


if __name__=="__main__":
  # 1759870
  # 9870
  # 590
  money = int(input('문자를 입력 하세요 : '))
  money_count(money)

  # if money >= 50000:
  #   print("5만원 개수 : ",money//50000)
  #   money %= 50000
  #   print("1만원 개수 : ",money//10000)
  #   money %= 10000
  #   print("5천원 개수 : ",money//5000)
  #   money %= 5000
  #   print("1천원 개수 : ",money//1000)
  #   money %= 1000
  #   print('500원 동전개수 : ',money//500)
  #   money %= 500
  #   print('100원 동전개수 : ',money//100)
  #   money %= 100
  #   print('50원 동전개수 : ',money//50)
  #   money %= 50
  #   print('10원 동전개수 : ',money//10)
  # elif money >= 10000:
  #   print("1만원 개수 : ",money//10000)
  #   money %= 10000
  #   print("5천원 개수 : ",money//5000)
  #   money %= 5000
  #   print("1천원 개수 : ",money//1000)
  #   money %= 1000
  #   print('500원 동전개수 : ',money//500)
  #   money %= 500
  #   print('100원 동전개수 : ',money//100)
  #   money %= 100
  #   print('50원 동전개수 : ',money//50)
  #   money %= 50
  #   print('10원 동전개수 : ',money//10)
  # elif money >= 5000:
  #   print("5천원 개수 : ",money//5000)
  #   money %= 5000
  #   print("1천원 개수 : ",money//1000)
  #   money %= 1000
  #   print('500원 동전개수 : ',money//500)
  #   money %= 500
  #   print('100원 동전개수 : ',money//100)
  #   money %= 100
  #   print('50원 동전개수 : ',money//50)
  #   money %= 50
  #   print('10원 동전개수 : ',money//10)
  # elif money >= 1000:
  #   print("1천원 개수 : ",money//1000)
  #   money %= 1000
  #   print('500원 동전개수 : ',money//500)
  #   money %= 500
  #   print('100원 동전개수 : ',money//100)
  #   money %= 100
  #   print('50원 동전개수 : ',money//50)
  #   money %= 50
  #   print('10원 동전개수 : ',money//10)
  # elif money >= 500:
  #   print('500원 동전개수 : ',money//500)
  #   money %= 500
  #   print('100원 동전개수 : ',money//100)
  #   money %= 100
  #   print('50원 동전개수 : ',money//50)
  #   money %= 50
  #   print('10원 동전개수 : ',money//10)
  # elif money >= 100:
  #   print('100원 동전개수 : ',money//100)
  #   money %= 100
  #   print('50원 동전개수 : ',money//50)
  #   money %= 50
  #   print('10원 동전개수 : ',money//10)
  # elif money >= 50:
  #   print('50원 동전개수 : ',money//50)
  #   money %= 50
  #   print('10원 동전개수 : ',money//10)
  # elif money >= 10:
  #   print('10원 동전개수 : ',money//10)

  
  # money = 1759870
  # # money = 780
  # print("5만원 개수 : ",money//50000)
  # money %= 50000
  # print("1만원 개수 : ",money//10000)
  # money %= 10000
  # print("5천원 개수 : ",money//5000)
  # money %= 5000
  # print("1천원 개수 : ",money//1000)
  # money %= 1000
  # # 500 - 1
  # print('500원 동전개수 : ',money//500)
  # money %= 500
  # # 100 - 2
  # print('100원 동전개수 : ',money//100)
  # money %= 100
  # # 50 - 1
  # print('50원 동전개수 : ',money//50)
  # money %= 50
  # # 10 - 3
  # print('50원 동전개수 : ',money//10)