students = [
  {"no":1,"name":"홍길동"},
  {"no":2,"name":"유관순"},
  {"no":3,"name":"이순신"}
]

stuNo = len(students)

def stu_input(stuNo, students):
  while True:
    no = stuNo + 1
    print('no : ', no)
    name = input('학생 이름을 입력하세요.(0.이전페이지 이동)')
    if name == '0': break
    students.append({'no':no, 'name':name})
    stuNo += 1
  return stuNo

choice = 1
stuNo = stu_input(choice, students)
print(stuNo)