import datetime as dt
# member = 회원정보
# 아이디, 패스워드, 이름, 닉네임, 주소
# product = 상품정보
# 상품코드, 이름, 가격, 사이즈
# cart = 구매정보
# 아이디, 상품코드, 가격

# member.txt 파일 읽기
members = []
m_title = ['id', 'pw', 'name', 'nicName', 'address', 'money']
f = open('members.txt', 'r', encoding='utf-8')
while True:
  data = f.readline()
  if not data : break
  list_data = data[:-1].split(',')
  for indx, i in enumerate(list_data):
    if i.isdigit():
      if indx != 1:
        list_data[indx] = int(i)
  members.append(dict(zip(m_title, list_data)))
f.close()

# cart.txt 파일 읽기
cart = []
c_title = ['cno','id','name','pCode','pName','price','date']
f = open('cart.txt', 'r', encoding='utf-8')
while True:
  data = f.readline()
  if not data : break
  list_data = data[:-1].split(',')
  for indx, i in enumerate(list_data):
    if i.isdigit():
      if indx != 1:
        list_data[indx] = int(i)
  cart.append(dict(zip(c_title, list_data)))
f.close()
cartNo = len(cart)

product = [
  {
    'pno': 1,
    'pCode': 't001',
    'pName': '삼성TV',
    'price': 2000000,
    'color': 'black'
  },
  {
    'pno': 2,
    'pCode': 'g001',
    'pName': 'LG냉장고',
    'price': 3000000,
    'color': 'white'
  },
  {
    'pno': 3,
    'pCode': 'h001',
    'pName': '하만카돈스피커',
    'price': 500000,
    'color': 'gray'
  },
  {
    'pno': 4,
    'pCode': 'w001',
    'pName': '세탁기',
    'price': 1000000,
    'color': 'yellow'
  }
]




sesstion_info = None
p_title = ['번호', '아이디', '이름', '상품코드', '상품명', '가격', '구매일자']



##########################################################################
def buy(choice, cartNo):
  print(f'{product[choice - 1]['pName']} 를 구매하셨습니다.')
  print('구매내역에 등록했습니다..')
  print()
  c = {
  'cno': cartNo + 1,
  'id': sesstion_info['id'],
  'name': sesstion_info['name'],
  'pCode': product[choice - 1]['pCode'],
  'pName': product[choice - 1]['pName'],
  'price': product[choice - 1]['price'],
  'date': dt.datetime.now()
  }
  sesstion_info['money'] -= product[choice - 1]['price']
  cartNo += 1
  cart.append(c)
  # print('구매내역', cart)
  return cartNo

def member_save():
  f = open('members.txt', 'w', encoding='utf-8')
  for i in members:
    f.write(f'{i['id']},{i['pw']},{i['name']},{i['nicName']},{i['address']},{i['money']}\n')
  print('내용저장이 완료되었습니다.')
  f.close()
  cart_save()

def cart_save():
  f = open('cart.txt', 'w', encoding='utf-8')
  for i in cart:
    f.write(f'{i['cno']},{i['id']},{i['name']},{i['pCode']},{i['pName']},{i['price']},{i['date']}\n')
  print('내용저장이 완료되었습니다.')
  f.close()

##########################################################################
while True:
  input_id = input('아이디를 입력하세요. >> ')
  input_pw = input('패스워드를 입력하세요. >> ')

  for member in members:
    if member['id'] == input_id and member['pw'] == input_pw:
      print("SM SHOP에 오신것을 환영합니다.! ")
      sesstion_info = member
      break

  if sesstion_info == None:
    print("아이디 또는 패스워드가 일치하지 않습니다.! ")
  else:
    break
      
  # user_id, user_pw = 'aaa', '1111'
  # if user_id == input_id and user_pw == input_pw:
  #   print("SM SHOP에 오신것을 환영합니다.! ")
  #   break
  # else:
  #   print("아이디 또는 패스워드가 일치하지 않습니다.! ")

while True:
  print('\t[ SM-SHOP 프로그램 ]')
  print(f'\t닉네임 : {sesstion_info['nicName']}')
  print(f'\t금액 : {sesstion_info['money']:,d}')
  print('1. 삼성TV - 2,000,000원')
  print('2. LG냉장고 - 3,000,000원')
  print('3. 하만카돈스피커 - 500,000원')
  print('4. 세탁기 - 1,000,000원')
  print('7. 내용저장')
  print('8. 구매내역 출력')
  print('9. 금액충전')
  choice = int(input('구매하려는 상품번호를 입력하세요. >> '))
  if choice == 8:
    for i in p_title:
      print(f'{i}',end='\t')
    print()
    print('-' * 60)
    sum = 0
    for p in cart:
      for i in p:
        print(f'{p[i]}', end='\t')
        if i == 'price':
          sum += p[i]
      print()
    print(f'총 구매 금액 : {sum:,d}')
    print(f'총 구매 건수 : {len(cart)}')
  elif choice == 9:
    add_money = input('충전할 금액을 입력하세요. >> ')
    sesstion_info['money'] += int(add_money)
    print('충전이 완료 되었습니다.')
    print(f'잔액 : {sesstion_info['money']}')
  elif choice == 7:
    member_save()
  elif choice == 0:
    break
  elif choice >= len(product) + 1 or choice <= 0:
    continue
  else:
    cartNo = buy(choice, cartNo)

  
