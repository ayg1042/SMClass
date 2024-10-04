




if __name__=="__main__":
  s_title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수']
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
    print('5. 학생성적삭제')
    print('6. 등수처리')
    print('0. 종료')
    print('*' * 60)
    choice = input('원하는 번호를 입력하세요. (종료 0)>> ')

    if choice == "0": break
    elif choice == '1':
      while True:
        print('학생성적입력')
        name = input(f'{no}번 학생 이름 (취소 : 0) : ')
        if name == '0': break
        kor = int(input('국어점수 : '))
        eng = int(input('영어점수 : '))
        math = int(input('수학점수 : '))
        total = kor + eng + math
        avg = total/3
        rank = 0
        s = [no, name, kor, eng, math, total, avg, rank]
        students.append(s)
        no += 1
        s = []
    elif choice == '2':
      print('학생정보출력')
      print(f'{s_title[0]}\t{s_title[1]}\t{s_title[2]}\t{s_title[3]}\t{s_title[4]}\t{s_title[5]}\t{s_title[6]}\t{s_title[7]}')
      for i in students:
        print(f'{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}\t{i[5]}\t{i[6]:.2f}\t{i[7]}')
      print('-' * 60)
    elif choice == '3':
      seach = False
      while True:
        name = input('수정할 학생 이름 (종료 : 0): ')
        if name == '0': break
        for i in students:
          print(i)
          if name in i:
            target = i
            seach = True
            break
          else:
            seach = False
        if seach:
          while True:
            print(target[1],'학생 정보를 수정합니다. ')
            print('1. 국어')
            print('2. 영어')
            print('3. 수학')
            choice = input('수정할 과목을 선택하세요 (취소 : 0) : ')
            if choice == '0': break
            choice = int(choice)
            print(s_title[choice + 1],'점수 : ', target[choice + 1])
            number = int(input('점수를 입력하세요 : '))
            if input('수정하시겠습니까? (y/n)') == 'y':
              target[choice + 1] = number
              target[5] = target[2] + target[3] + target[4]
              target[6] = target[5]/3
            else:
              print('취소합니다.')
        else:
          print('없는 학생입니다.')
    elif choice == '4':
      pass
    elif choice == '5':
      pass
    elif choice == '6':
      pass