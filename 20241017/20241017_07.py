# member
m_title = ['id', 'pw', 'name', 'nicname', 'address', 'money']
members = []

# 파일 불러오기
f = open('20241017/member.csv', 'r', encoding='utf-8')

while True:
  data = f.readline()
  if not data: break
  data_list = data.strip().split(',')
  print(data_list)
  data_list[-1] = int(data_list[-1])
  members.append(dict(zip(m_title, data_list)))
f.close()


def sreach_id(members):
  name = input('검색할 데이터 >> ')
  name_list = []
  for i in members:
    if name in i['id']:
      name_list.append(i)
  return name_list

while True:
  print('1. 회원등록')
  print('2. 회원검색')
  choice = input('원하는 번호를 입력하세요. >> ')
  if choice == '0': break
  elif choice == '1':
    while True:
      chx = 0
      id = input('ID를 입력하세요 >> ')
      for m in members:
        if id in m['id']:
          print('동일한 아이디가 있습니다. 다시 입력하세요.')
          break
        else:
          chx = 1
      if chx == 1:
        break
    pw = input('PW를 입력하세요 >> ')
    name = input('이름을 입력하세요 >> ')
    nicName = input('닉네임을 입력하세요 >> ')
    money = int(input('충전금액을 입력하세요 >> '))
    m_list = [id, pw, name, nicName, money]
    members.append(dict(zip(m_title, m_list)))
    print(f'{id} 님 회원가입이 완료되었습니다.!')
    print(m_list)
  elif choice == '2':
    pass



# 아이디 겁색
# members 리스트에서
# 입력한 문자로 검색된 데이터를 모두 출력하시오.
# a가 들어가 있는 아이디를 출력하시오.
sreach_list = sreach_id(members)
print(f'{len(sreach_list)}개 검색 되었습니다. ')
for i in sreach_list:
  print(i['id'])