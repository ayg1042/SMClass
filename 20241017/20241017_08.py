import datetime as dt
import os

m_title = ['id', 'pw', 'name', 'nicname', 'address', 'money']
members = []

p_title = ["번호","아이디","이름","코드","상품명","가격","구매일자"]
product = [
  {"pno":1,"pCode":"t001","pName":"삼성TV","price":2000000,"color":"black"},
  {"pno":2,"pCode":"g001","pName":"LG냉장고","price":3000000,"color":"white"},
  {"pno":3,"pCode":"h001","pName":"하만카돈스피커","price":500000,"color":"gray"},
  {"pno":4,"pCode":"w001","pName":"세탁기","price":1000000,"color":"yellow"},
]

session_info = {}

# isfile : 파일 확인
# isdir  : 디렉토리 확인
# exists : 파일이 존재하는지

# cart data setting
def cart_setting():
  cart = []
  c_title = ['cno','id','name','pCode','pName','price','date']
  if os.path.exists('cart.txt'):
    f = open('cart.txt', 'r', encoding='utf-8')
    while True:
      data = f.readline()
      if not data: break
      data_list = data[:-1].split(',')
      for idx, i in enumerate(data_list):
        if i.isdigit() and idx != 1:
          data_list[idx] = int(i)
      cart.append(dict(zip(c_title, data_list)))
  else:
    print('저장된 CART 파일이 없습니다.')
    return cart
  return cart

# members data setting
def member_setting():
  members = []
  m_title = ['id', 'pw', 'name', 'nicName', 'address', 'money']
  if os.path.exists('members.txt'):
    f = open('members.txt', 'r', encoding='utf-8')
    while True:
      data = f.readline()
      if not data: break
      data_list = data[:-1].split(',')
      for idx, i in enumerate(data_list):
        if i.isdigit() and idx != 1:
          data_list[idx] = int(i)
      members.append(dict(zip(m_title, data_list)))
  else:
    print('Members 데이터가 없습니다.')
    return members
    
  return members

# product data setting
def product_setting():
  products = []
  p_title = ["pno","pCode","pName","price","color"]
  if os.path.exists('product.txt'):
    f = open('product.txt', 'r', encoding='utf-8')
    while True:
      data = f.readline()
      if not data: break
      data_list = data[:-1].split(',')
      for idx, i in enumerate(data_list):
        if i.isdigit():
          data_list[idx] = int(i)
      products.append(dict(zip(p_title, data_list)))
  else:
    print('product 데이터가 없습니다.')
    return products
    
  return products

# login_function
def login_func(members):
  while True:
    id = input('아이디를 입력하세요. >> ')
    pw = input('패스워드를 입력하세요. >> ')
    for i in members:
      if i['id'] == id and i['pw'] == pw:
        return i
    print('id, pw 잘못 입력 되었습니다. ')

# member add
def member_add(members, m_title):
  print('회원가입을 진행합니다.')
  member = []
  member.append(id_check(members))
  member.append(pw_check())
  for i in range(2, len(m_title)):
    member.append(input(f'{m_title[i]} 을 입력하세요. >> '))
  members.append(dict(zip(m_title, member)))
  print('회원가입이 완료 되었습니다.')

def id_check(members):
  chx = 0
  while True:
    id = input('ID를 입력하세요. >> ')
    for i in members:
      if i['id'].find(id) == -1: chx = 1
      else:
        chx = 0
        break
    if chx != 0: break
    else:
      print('이미 사용중인 아이디 입니다. 다시 입력하세요.')
  return id

def pw_check():
  while True:
    pw = input('PW를 입력하세요. (4자리) >> ')
    if len(pw) < 4: continue
    else: return pw

# save data
def save_data(members, cart, products):
  member_save(members)
  cart_save(cart)
  product_save(products)

def member_save(members):
  f = open('members.txt', 'w', encoding='utf-8')
  for i in members:
    f.write(f'{i['id']},{i['pw']},{i['name']},{i['nicName']},{i['address']},{i['money']}\n')
  print('member 내용저장이 완료되었습니다.')
  f.close()

def cart_save(cart):
  f = open('cart.txt', 'w', encoding='utf-8')
  for i in cart:
    f.write(f'{i['cno']},{i['id']},{i['name']},{i['pCode']},{i['pName']},{i['price']},{i['date']}\n')
  print('cart 내용저장이 완료되었습니다.')
  f.close()

def product_save(product):
  f = open('product.txt', 'w', encoding='utf-8')
  for i in product:
    f.write(f'{i['pno']},{i['pCode']},{i['pName']},{i['price']},{i['color']}\n')
  print('product 내용 저장이 완료되었습니다.')
  f.close()

# buy_product
def buy_product(cartNo, choice, member, cart):
  choice = int(choice)
  product = products[choice - 1]
  # print(product)
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

if __name__ == '__main__':
  cart = cart_setting()
  print(cart)
  members = member_setting()
  print(members)
  products = product_setting()
  print(products)
  cartNo = int(cart[-1]['cno']) + 1
  while True:
    print(' [ 메인화면 ] ')
    print('1. [로그인] ')
    print('2. [회원가입] ')
    print('3. [데이터 저장]')
    print('0. 종료')
    print('-' * 60)
    choice = input('원하는 번호를 입력하세요 >> ')
    if choice == '0': break
    elif choice == '1':
      member = login_func(members)
    elif choice == '2':
      member_add(members, m_title)
    elif choice == '3':
      save_data(members, cart, products)
  
  while True:
    print("           [ SM-SHOP ]")
    print(f"                       닉네임:{member['nicName']}님")
    print(f"                       금액 :{member['money']:,} 원")
    print('--- 상품 목록 ---')
    for idx, i in enumerate(products):
      print(f'{idx + 1}. {i['pName']:10} \t-- 가격 : {i['price']:,d}')
    print('00. 구매목록 확인')
    choice = input("구매하려는 상품번호를 입력하세요.>> ")
    if choice == '99': break
    elif choice == '00':
      show_cart(cart)
    else:
      buy_product(cartNo, choice, member, cart)