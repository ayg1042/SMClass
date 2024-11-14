


s_title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수']

def add_student(students):
  global no
  while True:
    print(' [ 학생 성적 입력 ]')
    print('-' * 60)
    name = input(f'{no}번 이름을 입력하세요. (종료 : 0) >>')
    if name == '0': return students
    kor = int(input('국어 점수를 입력하세요. >> '))
    eng = int(input('영어 점수를 입력하세요. >> '))
    math = int(input('수학 점수를 입력하세요. >> '))
    total = kor + eng + math
    avg = round(total/3, 2)
    rank = 0
    s = [no, name, kor, eng, math, total, avg, rank]
    students.append(s)
    no += 1
    print('-' * 60)

def show_student(students):
  print('[ 학생 성적 출력 ]')
  print('-' * 60)
  print(f'{s_title[0]}\t{s_title[1]}\t{s_title[2]}\t{s_title[3]}\t{s_title[4]}\t{s_title[5]}\t{s_title[6]}\t{s_title[7]}')
  for s in students:
    print(f'{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}')
  print('-' * 60)

def student_info_update(students):
  while True:
    print(' [ 학생 성적 수정 ] ')
    print('-' * 60)
    print(' 수정할 학생 정보를 검색합니다.')
    number = student_search(students)
    if not number:
      print('취소합니다.')
      break
    target = students[number - 1]
    print(target[1])
    print('1. 국어')
    print('2. 영어')
    print('3. 수학')
    choice = input('수정할 과목을 선택하세요. (취소 : 0)')
    if choice == '0': return
    choice = int(choice) + 1
    print(s_title[choice],'점수 : ', target[choice])
    

def student_search(students):
  swith = False
  number = 0
  while True:
    print(' [ 학생 성적 검색 ] ')
    print('-' * 60)
    name = input('검색할 학생 이름을 입력하세요. (종료 : 0) >> ')
    
    if name == '0':
      break
    else:
      for i in students:
        if name in i:
          swith = True
        else:
          swith = False

    if swith:
      for s in students:
        if name in s:
          print(f'{name} 학생 성적입니다.')
          print(f'{s_title[0]}\t{s_title[1]}\t{s_title[2]}\t{s_title[3]}\t{s_title[4]}\t{s_title[5]}\t{s_title[6]}\t{s_title[7]}')
          print(f'{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}')
          number = s[0]
    else:
      print('없는 학생입니다.')
  return number




if __name__=="__main__":
  students = []
  global no
  no = 1
  # 학생성적프로그램
  while True:
      print('[ 학생성적 프로그램 ]')
      print('*' * 60)
      print('1. 학생성적입력')
      print('2. 학생성적출력')
      print('3. 학생성적수정')
      print('4. 학생성적검색')
      print('0. 종료')
      print('*' * 60)
      choice = input('원하는 번호를 입력하세요. (종료 0)>> ')

      if choice == '1':
        students = add_student(students)
      elif choice == '2':
        show_student(students)
      elif choice == '3':
        student_info_update(students)
      elif choice == '4':
        student_search(students)
      elif choice == '0':
        break