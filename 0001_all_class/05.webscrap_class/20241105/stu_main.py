import stu_func as sf

while True:
  print(' [ 학생성적 프로그램 ] ')
  print(' 1. 학생성적입력')
  print(' 2. 학생성적출력')
  print(' 3. 학생성적검색')
  print(' 4. 학생성적정렬')
  print(' 5. 등수처리')
  choice = input('원하는 번호를 선택하세요. >> ')

  if choice == '1':
    sf.add_data()
  elif choice == '2':
    sf.show_data()
  elif choice == '3':
    chek = sf.sreach_data()
    if chek == -1:
      print('검색에 실패 했습니다.')
  elif choice == '4':
    sf.sort_stu()
  elif choice == '5':
    sf.rank_setting()
  elif choice == '0':
    break