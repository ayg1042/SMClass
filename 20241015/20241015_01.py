def calc(st, end):
  for i in range(st, end + 1):
    print(f'{i} 단')
    for j in range(1, 10):
      print(f'{i} * {j} = {i * j}')

# def plus(s1, s2):
#   sum = s1 + s2
#   print('합계 : ', sum)
#   return sum

def plus(k = 10, m = 5):
  print('k : ', k)
  print('m : ', m)

print(plus)




# def plus(a, *s1):
#   print('a : ', a)
#   for i in s1:
#     print(i)
#   print(type(s1))

# plus(1, 2, 3, 4, 5, 6, 7, 8, 9)

# st = 2
# end = 9
# calc(st, end)

# for i in range(st, end + 1):
#   print(f'{i} 단')
#   for j in range(1, 10):
#     print(f'{i} * {j} = {i * j}')