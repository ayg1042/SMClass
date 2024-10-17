# 딕셔너리로 입력
sub = ['no', 'name', 'kor', 'eng', 'math', 'total', 'avg', 'rank']
subject = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수']
students = []

f = open('20241017/students.txt', 'r', encoding='utf-8')
while True:
  data = f.readline()
  if not data: break
  s = data.strip().split(',')
  for idx, i in enumerate(s):
    if idx == 1: continue
    elif idx == 7: s[6] == float(i)
    else: s[i] = int(s[i])
    # if i.isdigit()
  print(s)
f.close()