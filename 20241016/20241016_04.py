members = [
  {
  'id': 'aaa',
  'pw': '1111',
  'name': '홍길동',
  'nicName': '길동스',
  'address': '서울시',
  'money': 1000000000
  },
  {
  'id': 'bbb',
  'pw': '2222',
  'name': '유관순',
  'nicName': '관순스',
  'address': '부산시',
  'money': 10000000
  },
  {
  'id': 'ccc',
  'pw': '3333',
  'name': '이순신',
  'nicName': '순신스',
  'address': '경기도',
  'money': 10000000
  },
  {
  'id': 'ddd',
  'pw': '4444',
  'name': '강감찬',
  'nicName': '감찬스',
  'address': '인천시',
  'money': 10000000
  },
  {
  'id': 'admin',
  'pw': 'admin',
  'name': '김구',
  'nicName': '구스',
  'address': '서울시',
  'money': 10000000
  },
]
# members 딕셔너리파일을 메모장에 csv파일 형태로 저장하시오.
f = open('members.txt', 'w', encoding='utf-8')
for i in members:
  f.write(f'{i['id']},{i['pw']},{i['name']},{i['nicName']},{i['address']},{i['money']}\n')
f.close()



# a = ['no', 'name', 'kor', 'eng']
# b = [1, '홍길동', 100, 100]
# print(dict(zip(a, b)))