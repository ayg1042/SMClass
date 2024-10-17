a = ['1', '홍길동', '69', '89', '73', '231', '77', '1']
b = ['1', '69', '89', '73', '231', '77', '1']
t_title = ['no', 'name', 'kor', 'eng', 'math', 'total', 'avg', 'rank']
c = []

def t_float(n):
  try:
    int(n)
    return True
  except:
    return False



# b의 리스트 float변경
for i in b:
  if t_float(i): i = int(i)
  else: i = float(i)
  c.append(i)
print(c)

for idx, i in enumerate(a):
  if i.isdigit(): print(f'{idx}번째 {i}는 숫자입니다.')
  else: print(f'{idx}번째 {i}는 문자입니다.')