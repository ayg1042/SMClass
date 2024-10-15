import s_function as sf

# students 리스트 타입
students = [
  {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
  {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
  {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
  {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
  {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
]
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