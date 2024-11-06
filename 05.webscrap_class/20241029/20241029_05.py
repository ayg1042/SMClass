
title = ['e_id', 'e_name', 'salary']
a = [192, 'Sarah Bell', 4000.0]
aa = [
  (196, 'Alana Walsh', 3100.0),
  (125, 'Julia Nayer', 3200.0),
  (180, 'Winston Taylor', 3200.0),
  (194, 'Samuel McCain', 3200.0),
  (138, 'Stephen Stiles', 3200.0)
]

print(dict(zip(title, a)))

# dict 타입으로 저장하세요.
b = []
for i in aa:
  b.append(dict(zip(title, i)))
print(b)


# title = ['e_id', 'e_name', 'salary']
# a = [192, 'Sarah Bell', 4000.0]
# print(zip(title, a))
# print(dict(zip(title, a)))



# "select * from employees where emp_name like '%a%'"
# 문자 변수 출력
# name = '홍길동'
# a = '안녕하세요. 이름은 %s'%name
# print('hello. my name is {}'.format(name))
# print(f'hello. my name is {name}')


# a = 1
# b = 2

# a_list = [a, b]

# print(type(a_list))
# a_tuple = (a, b)
# print(type(a_tuple))

# # 튜플 1개만지정할 때 ,를 넣어줘야함.
# b_tuple = (a,)
# print(type(b_tuple))
# b_list = [a]
# print(type(b_list))
