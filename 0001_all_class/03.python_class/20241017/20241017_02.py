subject = ['이름', '국어', '영어', '수학', '합계']
students = []

### 함수선언 ###
def stuScore_update():
  print(f'현재 {subject[choice]}점수 :')


#---------------
while True:
  print('1. 학생성적 입력')
  print('2. 학생성적 출력')
  print('3. 학생성적 수정')
  choice = input('원하는 번호를 입력하세요. >> ')
  if choice == '0': break
