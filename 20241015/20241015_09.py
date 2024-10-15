# 퀴즈
a = [1, 2, 3, 4, 5]
# a리스트에 전부 10을 더해서 리스트에 담아 출력
# 리스트 내포, 람다식 사용
b = [i + 10 for i in a]
print(b)
c = list(map(lambda i : i + 10, a))
print(c)



# a = [1, 2, 3, 4]
# b = [10, 20, 30, 40]
# a + b = [11, 22, 33, 44]람다식 구현
# 함수구현
# def func(a, b):
#   c = []
#   for i in range(len(a)):
#     c.append(a[i] + b[i])
#   d = [i + j for i, j in zip(a, b)]
#   return c

# aa = [i + j for i, j in zip(a, b)]
# 람다식구현

# map(lambda 매개변수1, 매개변수2:리턴값, 복합자료형1, 복합자료형2) 
# aArr = list(map(lambda i, j : i+j), a, b)


# 밑 두연산 같은거임
# def func(v1, v2):
#   return v1 * v2

# lambda v1, v2 : v1 * v2



# def func(v):
#   if v % 2 == 0:
#     return True
#   else:
#     return False
  

# 람다식 변경
# aArr = [1, 2, 3, 4]
# bArr = list(filter(lambda x: x%2 == 0, aArr))
# print(bArr)

# aArr 값중에 2의 배수인 경우만 리턴
# aArr = [1, 2, 3, 4]
# bArr = list(filter(func, aArr))
# print(bArr)



# def func(v):
#   if v%2 == 0:
#     return True
#   else:
#     return False

# aArr = [1, 2, 3, 4]
# bArr = []
# for i in aArr:
#   if func(i) != None:
#     bArr.append(func(i))
# print(bArr)


# map 함수 map(함수, 리스트) : 리스트의 내용을 1개식 함수에 전달해서 결과값을 리스트로 저장
# aArr = [1, 2, 3, 4]
# bArr = list(map(func, aArr))
# print(bArr)
# bArr = list(map(lambda x: x * 2, aArr))

# 리스트 내포.
# aArr = [1, 2, 3, 4]
# bArr =[func(i) for i in aArr]
# print(bArr)


# 기본적인 함수 사용
# print(func(2))
# aArr = [1, 2, 3, 4]
# bArr = []
# for a in aArr:
#   bArr.append(func(a))
# print(bArr)

