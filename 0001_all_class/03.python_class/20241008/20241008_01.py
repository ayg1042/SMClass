
def add_student(students):
  No = len(students) + 1
  while True:
    name = input(f"{No}번 학생이름을 입력하세요. (종료 : 0) >> ")
    if name =='0': return 0
    kor = int(input('국어 점수를 입력하세요. >> '))
    eng = int(input('영어 점수를 입력하세요. >> '))
    math = int(input('수학 점수를 입력하세요. >> '))
    total = kor + eng + math
    avg = total/3
    rank = 0
    student = [No, name, kor, eng, math, total, avg, rank]
    students.append(student)
    No += 1
  
def show_students(students, title):
  print('-' * 60)
  for i in title:
    print(i, end='\t')
  print()
  print('-' * 60)
  for i in students:
    print(f'{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}\t{i[5]}\t{i[6]:.2f}\t{i[7]}\t')
  
def sreach_student(students, T=1):
  no = 0
  while True:
    sch = False
    name = input('학생 이름을 입력하세요 (종료 : 0) >> ')
    if name == '0': return 0
    for i in students:
      if name in i:
        sch = True
        no = i[0]
        print(f'{name} 학생의 정보입니다.')
        print('-' * 60)
        print(f'{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}\t{i[5]}\t{i[6]:.2f}\t{i[7]}\t')
    if not sch:
      print('찾는 학생이 없습니다.')
    if not T:
      return no

def update_students(students, title, no):
  while True:
    print('[학생정보수정]')
    print('1. 국어')
    print('2. 영어')
    print('3. 수학')
    choice = input('수정할 번호를 선택하세요. >> ')
    print(f'{title[int(choice) + 1]} 점수 입니다. : {students[no - 1][int(choice) + 1]}')
    chg = int(input('수정할 점수를 입력하세요 >> '))
    students[no - 1][int(choice) + 1] = chg
    total = students[no - 1][2] + students[no - 1][3] + students[no - 1][4]
    avg = total/3
    students[no - 1][5] = total
    students[no - 1][6] = avg
    if input('그만하기 0 >> ') == '0': break

def delete_student(students, no):
  print(f'{students[no - 1][1]} 학생을 제거합니다.')
  if input('제거하면 되돌릴 수 없습니다. (y/n)') == 'y':
    del students[no - 1]
  else: print('취소하였습니다.')

def rank_students(students):
  print('등수처리')
  no = 1
  for i in range(len(students)):
    students[i][-1] = 1
    for j in range(len(students)):
      if students[j][-3] > students[i][-3]:
        students[i][-1] += no


if __name__ == "__main__":
  students = []
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
    print("0. 프로그램 종료")
    print("-"*60)
    choice = input("원하는 번호를 입력하세요.(0.종료)>> ")

    if choice == '1':
      add_student(students)
    elif choice == '2':
      show_students(students, title)
    elif choice == '3':
      update_students(students, title, sreach_student(students, 0))
    elif choice == '4':
      sreach_student(students)
    elif choice == '5':
      delete_student(students, sreach_student(students, 0))
    elif choice == '6':
      rank_students(students)
    elif choice == '0':
      print('프로그램을 종료합니다.')
      break