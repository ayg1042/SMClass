
def stu_add(stuNo, students):
  while True:
    no = stuNo + 1
    name = input(f'{no}번 학생이름을 입력하세요. (0. 뒤로가기) : ')
    if name == '0': break
    score = []
    total = 0
    for i in range(2, len(s_title) - 3):
      s = int(input(f'{s_title[i]} 점수를 입력하세요. >> '))
      score.append(s)
      total += s
    avg = total/(len(s_title) - 5)
    # print(score)
    students.append({
      'no':no,
      'name':name,
      'kor': score[0],
      'eng': score[1],
      'math': score[2],
      'total': total,
      'avg': avg,
      'rank': 0
    })
    stuNo += 1
  return stuNo

def stu_output(students):
  for i in s_title:
    print(i, end='\t')
  print()
  print('-' * 60)
  for i in students:
    for j in i:
      print(f'{i[j]}', end='\t')
    print()

def stu_update(students):
  student = stu_seach(students)
  e_title = list(student.keys())
  student = student[1]
  if student != 0:
    print('1. 국어')
    print('2. 영어')
    print('3. 수학')
    choice = int(input('수정할 과목을 선택하세요. >> '))
    if choice >= 4 or choice <= 0:
      print('잘못된 값 입니다.')
    print(f'{s_title[choice + 1]}점수 : {student[e_title[choice + 1]]} ')
    chg = int(input('변경할 점수를 입력하세요. >> '))
    student[e_title[choice + 1]] = chg
    student['total'] = student['kor'] + student['eng'] + student['math']
    student['avg'] = student['total'] / 3
    stu_output([student])

def stu_seach(students):
  name = input('학생 이름을 입력하세요. >> ')
  chx = 0
  re = 0
  stu_no = 0
  for idx,i in enumerate(students):
    if i['name'] == name:
      chx = 1
      stu_output([i])
      re = i
      stu_no = idx
  if chx == 0:
    print(f'{name} 학생이 없습니다.')
    return 0
  else:
    return [stu_no, re]

def stu_delet(students):
  student = stu_seach(students)
  if student[1] == 0:
    print('없는 학생입니다.')
    return 0
  target = students[student[0]]

  print(f'{target['name']}을 삭제합니다.')
  if input('삭제 하시겠습니까? (y/n)').lower() == 'y':
    del students[student[0]]
    print('삭제 되었습니다.')
  else:
    print('취소되었습니다.')

def stu_rank(students):
  for i in students:
    rank = 1
    for j in students:
      if i['total'] < j['total']:
        rank += 1
    i['rank'] = rank
  
def stu_sort(students):
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
      students.sort(key=lambda x:x['total'], reverse=True)
    elif choice == '4':
      students.sort(key=lambda x:x['total'])
    elif choice == '5':
      students.sort(key=lambda x:x['no'], reverse=True)
    elif choice == '6':
      students.sort(key=lambda x:x['no'])


if __name__ == '__main__':
  # students 리스트 타입
  students = [
    {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
    {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
    {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
    {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
    {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
  ]
  s_title = ['번호','이름','국어','영어','수학','합계','평균','등수'] #전역변수
  choice = 0 # 전역변수
  chk = 0    # 체크변수
  count = 1  # 성적처리
  stuNo = len(students)  # 리스트에 학생이 있으면, 그 인원으로 변경
  no=0;name="";kor=0;eng=0;math=0;total=0;avg=0;rank=0 #성적처리변수

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
      stuNo = stu_add(stuNo, students)
    elif choice == '2':
      stu_output(students)
    elif choice == '3':
      stu_update(students)
    elif choice == '4':
      stu_seach(students)
    elif choice == '5':
      stu_delet(students)
    elif choice == '6':
      stu_rank(students)
    elif choice == '7':
      stu_sort(students)
    elif choice == '0':
      print('종료')
      break