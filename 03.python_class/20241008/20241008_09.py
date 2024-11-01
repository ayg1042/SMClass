








if __name__ == '__main__':
  students = [
    {'no': 1, 'name': "홍길동", 'kor': 100, 'eng': 100, 'math': 99, 'total': 299, 'avg': 99.67, 'rank': 0},
    {'no': 2, 'name': "유관순", 'kor': 80, 'eng': 80, 'math': 85, 'total': 245, 'avg': 81.67, 'rank': 0},
    {'no': 3, 'name': "이순신", 'kor': 90, 'eng': 90, 'math': 91, 'total': 271, 'avg': 90.33, 'rank': 0},
    {'no': 4, 'name': "강감찬", 'kor': 60, 'eng': 65, 'math': 67, 'total': 192, 'avg': 64.00, 'rank': 0},
    {'no': 5, 'name': "김구", 'kor': 100, 'eng': 100, 'math': 84, 'total': 284, 'avg': 94.67, 'rank': 0}
  ]
  title = ['번호', '이름', '국어', '영어', '수학', '합계', '통계', '등수']
  no = len(students) + 1

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
    if choice == '0': break
    elif choice == '2':
      print(' [ 학생정보 출력 ] ')
      print('-' * 60)
      for i in title:
        print(i, end='\t')
      print()
      print('-' * 60)
      for i in students:
        print(f'{i['no']}\t{i['name']}\t{i['kor']}\t{i['eng']}\t{i['math']}\t{i['total']}\t{i['avg']:.2f}\t{i['rank']}\t')

    elif choice == '7':
      while True:
        print(' [ 학생성적 정렬 ] ')
        print('1. 이름 순차정렬')
        print('2. 이름 역순정렬')
        print('3. 합계 순차정렬')
        print('4. 합계 역순정렬')
        print('5. 번호 순차정렬')
        print('0. 이전페이지 이동')
        print('-' * 40)
        choice = input('원하는 번호를 입력하세요. >> ')
        if choice == '0': break

        if choice == '1':
          students.sort(key=lambda x:x['name'])
        elif choice == '2':
          students.sort(key=lambda x:x['name'], reverse=True)
      



  # 학생성적 입력부분을 구현하시오.
  # dict타입으로 입력할것
  # 번호, 이름, 국어, 영어, 수학, 합계, 평균, 등수
  # 입력이 완료되면 출력이 되도록 하시오.
  # no = 1
  # while True:
  #   name = input('이름을 입력하세요 0종료>> ')
  #   if name == '0': break
  #   kor = int(input('국어 점수 : '))
  #   eng = int(input('영어 점수 : '))
  #   math = int(input('수학 점수 : '))
  #   total = kor + eng + math
  #   avg = total/3
  #   rank = 0
  #   s = {
  #     "번호": no,
  #     '이름': name,
  #     '국어': kor,
  #     '영어': eng,
  #     '수학': math,
  #     '합계': total,
  #     '평균': avg,
  #     '등수': rank
  #     }
  #   students.append(s)
  #   no += 1
  #   for i in s.keys():
  #     print(i, end='\t')
  #   print()
  #   print('-' * 60)
  #   for i in students:
  #     for j in i.keys():
  #       if type(i[j]) == float: print(f'{i[j]:.2f}', end='\t')
  #       else: print(f'{i[j]}', end='\t')
  #     print()
