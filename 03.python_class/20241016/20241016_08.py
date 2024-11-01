import datetime as dt

# sm shop

# members data setting
def member_setting():
  members = []
  m_title = ['id', 'pw', 'name', 'nicName', 'address', 'money']
  f = open('members.txt', 'r', encoding='utf-8')
  while True:
    data = f.readline()
    if not data: break
    data_list = data[:-1].split(',')
    for idx, i in enumerate(data_list):
      if i.isdigit() and idx != 1:
        data_list[idx] = int(i)
    members.append(dict(zip(m_title, data_list)))
  return members

# cart data setting
def cart_setting():
  cart = []
  c_title = ['cno','id','name','pCode','pName','price','date']
  f = open('cart.txt', 'r', encoding='utf-8')
  while True:
    data = f.readline()
    if not data: break
    data_list = data[:-1].split(',')
    for idx, i in enumerate(data_list):
      if i.isdigit() and idx != 1:
        data_list[idx] = int(i)
    cart.append(dict(zip(c_title, data_list)))
  return cart

# login_function
def login_func(members):
  while True:
    id = input('아이디를 입력하세요. >> ')
    pw = input('패스워드를 입력하세요. >> ')
    for i in members:
      if i['id'] == id and i['pw'] == pw:
        return i
    print('id, pw 잘못 입력 되었습니다. ')

# buy_product
def buy_product(cartNo, choice, member, cart):
  choice = int(choice)
  product = products[choice - 1]
  print(product)
  print(f'상품 : {product['pName']} 구매 했습니다.')
  member['money'] -= product['price']
  get_data = {
    'cno': cartNo,
    'id': member['id'],
    'name': member['name'],
    'pCode': product['pCode'],
    'pName': product['pName'],
    'price': product['price'],
    'date': dt.datetime.now()
  }
  cart.append(get_data)
  cartNo += 1
  return cartNo

# show_cart data
def show_cart(cart):
  c_title = ['cno','id','name','pCode','pName','price','date']
  # print(cart)
  for i in cart:
    for j in c_title:
      print(f'{i[j]}', end='\t')
    print()
  print()

# save_data
def save_data():
  member_save()
  cart_save()

def member_save():
  f = open('members.txt', 'w', encoding='utf-8')
  for i in members:
    f.write(f'{i['id']},{i['pw']},{i['name']},{i['nicName']},{i['address']},{i['money']}\n')
  print('내용저장이 완료되었습니다.')
  f.close()

def cart_save():
  f = open('cart.txt', 'w', encoding='utf-8')
  for i in cart:
    f.write(f'{i['cno']},{i['id']},{i['name']},{i['pCode']},{i['pName']},{i['price']},{i['date']}\n')
  print('내용저장이 완료되었습니다.')
  f.close()


products = [
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


if __name__=='__main__':
  print('-' * 50)
  print('회원 정보 불러오기')
  members = member_setting()
  print('-' * 50)
  print('카트 정보 불러오기')
  cart = cart_setting()
  print('-' * 50)
  member = login_func(members)
  cartNo = int(cart[-1]['cno']) + 1
  while True:
    print('\t\t[ SM SHOP ]')
    print(f'\t\t{member['nicName']}님 안녕하세요. ')
    print(f'\t\t잔액 : {member['money']:,d}')
    print('--- 상품 목록 ---')
    for idx, i in enumerate(products):
      print(f'{idx + 1}. {i['pName']:10} \t-- 가격 : {i['price']:,d}')
    print('00. 구매목록 확인')
    print('99. Save_Data')
    choice = input('선택 : >> ')
    if choice == '0': break
    elif choice == '00': show_cart(cart)
    elif choice == '99': save_data()
    elif int(choice) > len(products) or int(choice) < -1:
      print('다시 입력해 주세요') 
    else:
      cartNo = buy_product(cartNo, choice, member, cart)
    