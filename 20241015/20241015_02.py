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

def stu_input(stuNo, students):
  while True:
    print('[ 학생성적입력 ]')
    no = stuNo + 1
    name = input('학생 이름을 입력하세요. (0. 이전화면) >> ')
    if name == '0': break
    score = []
    total = 0
    for i in range(3):
      k = int(input(f'{s_title[i + 2]} 점수를 입력하세요. >> '))
      total += k
      score.append(k)
    avg = total / 3
    rank = 0
    s = {
      'no': no,
      'name': name,
      'kor': kor,
      'eng': eng,
      'math': math,
      'total': total,
      'avg': avg,
      'rank': rank
    }
    students.append(s)
    print(f'{name} 학생성적이 저장되었습니다.')
    stuNo += 1
    print()
  return stuNo

### 실제 프로그램 시작 부분

choice = input('원하는 번호를 입력하세요. >> ')

if choice == '1':
  stuNo = stu_input(stuNo, students)