
def add_student(students):
  if len(students): No = len(students) + 1
  No = 0
  while True:
    name = input(f"{No}번 학생이름을 입력하세요. (종료 : 0) >> ")
    if name =='0': return 0
    kor = int(input('국어 점수를 입력하세요. >> '))
    eng = int(input('영어 점수를 입력하세요. >> '))
    math = int(input('수학 점수를 입력하세요. >> '))
    total = kor + eng + math
    avg = total/3
    rank = 0
    student = {
      'no': No,
      'name': name,
      'kor': kor,
      'eng': eng,
      'math': math,
      'total': total,
      'avg': avg,
      'rank': rank
      }
    students.append(student)
    No += 1
  
def show_students(students, title):
  print('-' * 60)
  for i in title:
    print(i, end='\t')
  print()
  print('-' * 60)
  for i in students:
    print(f'{i['no']}\t{i['name']}\t{i['kor']}\t{i['eng']}\t{i['math']}\t{i['total']}\t{i['avg']:.2f}\t{i['rank']}\t')
  
def sreach_student(students, T=1):
  no = 0
  while True:
    sch = False
    name = input('학생 이름을 입력하세요 (종료 : 0) >> ')
    if name == '0': return 0
    for i in students:
      if name in i['name']:
        sch = True
        no = i
        print(f'{name} 학생의 정보입니다.')
        print('-' * 60)
        print(f'{i['no']}\t{i['name']}\t{i['kor']}\t{i['eng']}\t{i['math']}\t{i['total']}\t{i['avg']:.2f}\t{i['rank']}\t')
    if not sch:
      print('찾는 학생이 없습니다.')
    if not T:
      return no

def update_students(title, no):
  cho_dic = {
    '1': 'kor',
    '2': 'eng',
    '3': 'math'
    }
  if not no: return 0
  while True:
    print('[학생정보수정]')
    print('1. 국어')
    print('2. 영어')
    print('3. 수학')
    choice = input('수정할 번호를 선택하세요. (돌아가기 0) >> ')
    if choice == '0': break
    print(f'{title[int(choice) + 1]} 점수 입니다. : {no[cho_dic[choice]]}')
    chg = int(input('수정할 점수를 입력하세요 >> '))
    no[cho_dic[choice]] = chg
    total = no['kor'] + no['eng'] + no['math']
    avg = total/3
    no['total'] = total
    no['avg'] = avg

def delete_student(students, no):
  print(f'{no['name']} 학생을 제거합니다.')
  for idx, data in enumerate(students):
    if data == no:
      del_che = idx
  if input('제거하면 되돌릴 수 없습니다. (y/n)') == 'y':
    del students[del_che]
  else: print('취소하였습니다.')
# 6~7번 해야함
def rank_students(students):
  print('등수처리')
  for i in range(len(students)):
    no = 1
    for j in range(len(students)):
      if students[i]['total'] < students[j]['total']:
        no += 1
    students[i]['rank'] = no

def sort_students(students):
  while True:
        print(' [ 학생성적 정렬 ] ')
        print('1. 이름 순차정렬')
        print('2. 이름 역순정렬')
        print('3. 합계 순차정렬')
        print('4. 합계 역순정렬')
        print('5. 번호 순차정렬')
        print('6. 번호 역순정렬')
        print('0. 이전페이지 이동')
        print('-' * 40)
        choice = input('원하는 번호를 입력하세요. >> ')
        if choice == '0': break

        if choice == '1':
          students.sort(key=lambda x:x['name'], reverse=True)
        elif choice == '2':
          students.sort(key=lambda x:x['name'])
        elif choice == '3':
          students.sort(key=lambda x:x['total'], reversed=True)
        elif choice == '4':
          students.sort(key=lambda x:x['total'])
        elif choice == '5':
          students.sort(key=lambda x:x['no'], reversed=True)
        elif choice == '6':
          students.sort(key=lambda x:x['no'])


if __name__ == "__main__":
  students = [
    {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
    {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
    {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
    {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
    {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
  ]
  title = ['번호', '이름', '국어', '영어', '수학', '합계', '통계', '등수']

  while True:
    print("[ 학생성적프로그램 ]")
    print("-"*60)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("4. 학생성적검색")
    print("5. 학생성적삭제")
    print("6. 등수처리")
    print("7. 학생성적정렬")
    print("0. 프로그램 종료")
    print("-"*60)
    choice = input("원하는 번호를 입력하세요.(0.종료)>> ")

    if choice == '1':
      add_student(students)
    elif choice == '2':
      show_students(students, title)
    elif choice == '3':
      update_students(title, sreach_student(students, 0))
    elif choice == '4':
      sreach_student(students)
    elif choice == '5':
      delete_student(students, sreach_student(students, 0))
    elif choice == '6':
      rank_students(students)
    elif choice == '7':
      sort_students(students)
    elif choice == '0':
      print('프로그램을 종료합니다.')
      break