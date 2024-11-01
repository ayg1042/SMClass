import s_function as sf

# students 리스트 타입
s_title = ['no', 'name', 'kor', 'eng', 'math', 'total', 'avg', 'rank']
students = []
f = open('students.txt', 'r', encoding="utf-8")
while True:
  data = f.readline()
  if not data: break
  data_list = data[:-1].split(',')
  for idx, i in enumerate(data_list):
    print(i)
    if idx == 1: continue
    elif idx == 6:data_list[idx] = float(i)
    elif i == '': continue
    else: data_list[idx] = int(i)
  students.append(dict(zip(s_title, data_list)))
print('학생정보 불러오기')
print(students)
f.close()

choice = 0 # 전역변수
stuNo = len(students)  # 리스트에 학생이 있으면, 그 인원으로 변경
s_title = ['번호','이름','국어','영어','수학','합계','평균','등수'] #전역변수
chk = 0    # 체크변수
count = 1  # 성적처리
no=0;name="";kor=0;eng=0;math=0;total=0;avg=0;rank=0 #성적처리변수


# -------------- 프로그램 시작 -----------------
# 학생성적프로그램
while True:
  choice = sf.title_program()        # 메뉴출력함수 호출
  if choice == "1":
    stuNo = sf.stu_input(stuNo, students)                   # 학생성적입력함수 호출
  elif choice == "2":
    sf.stu_output(students)
  elif choice == "3":
    sf.stu_update(students)
  elif choice == "4":
    sf.stu_select(students)
  elif choice == "5":
    sf.stu_delete(students)
  elif choice == "6":
    sf.stu_rank(students)
  elif choice == "7":
    sf.stu_sort(students)
  #-----------------------
  # 3,4,5,6
  #-----------------------
  elif choice == "0":
    print("[ 프로그램 종료 ]")
    print("프로그램을 종료합니다.")
    break
# 학생성적 입력부분을 구현하시오.
# dict타입으로 입력을 할것
# 번호,이름,국어,영어,수학,합계,평균,등수
# 입력이 완료되면 출력이 바로 되도록 하시오.