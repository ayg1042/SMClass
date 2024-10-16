# 파일 with
# close()를 하지 않아도 된다.
with open('aa.txt', 'w', encoding='utf-8') as f:
  f.write('안녕하세요.')

# 파일 이어쓰기 - a

# while True:
#   print(' [ 메모장 ] ')
#   data = input('저장하려는 글자를 입력하세요. >> ')
#   f = open('aa.txt', 'a',encoding='utf-8')
#   f.write(data+'\n')
#   f.close

# 파일쓰기 - w

# while True:
#   print(' [ 메모장 ] ')
#   data = input('저장하려는 글자를 입력하세요. >> ')
#   f = open('aa.txt', 'w',encoding='utf-8')
#   f.write(data)

# for i in range(1, 11):
#   data = f'{i}. 안녕하세요.\n'
#   f.write(data)
# print('글쓰기 종료')

# f.write('안녕하세요1\n')
# f.write('안녕하세요2\n')
# f.write('안녕하세요3')
# print('글쓰기 종료')

# 파일 읽기 - r
# 위치에 파일이 없으면 에러
# f = open('20241016/b.txt', 'r',encoding='utf-8')

# 3. read()
# for i in f:
#   print(i)
# line = f.read()
# print(line)

# 2. readlines() - 모든글을 읽어오기
# lines = f.readlines()
# for i in lines:
#   print(i.strip())

# 1. readline() 한줄식 읽음
# workspace단에서 인터프린터가 돔
# 가장 바깥 폴더의 위치에서 파일을 찾음.
# f = open('a.txt', 'r',encoding='utf-8')
# f = open('C:/aaa/a.txt', 'r',encoding='utf-8')
# f = open('20241016/a.txt', 'r',encoding='utf-8')
# while True:
#   line = f.readline()
#   if not line: break
#   print(line.strip()) # \n 값을 생략
# line = f.readline()
# print(line)
# f.close