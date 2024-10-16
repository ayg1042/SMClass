# 파일 쓰기
f = open('20241016/img/1.jpg', 'rb')
fData = f.read()
f.close()
print('파일읽기성공')
ff = open('20241016/img/2.jpg', 'wb')
lend = ff.write(fData)
print(f'파일 크기 : {lend} 바이트')
ff.close()

# 파일(바이너리파일)을 읽기
# f = open('20241016/img/1.jpg', 'rb')
# fData = f.read()
# f.close()
# print('파일읽기성공')

# 문서파일 읽기, 쓰기, 이어쓰기, 내용을 복사해서 쓰기
# txt내용 복사
# f = open('students.txt', 'r', encoding='utf-8')
# ff = open('students2.txt', 'w', encoding='utf-8')
# while True:
#   line = f.readline()
#   if not line: break
#   ff.write(line)
#   print(line.strip())
# f.close()
# ff.close()

# a b a a