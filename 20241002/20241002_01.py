



if __name__=="__main__":
  
  # 문자열
  # 문자열 숫자
  a = "123"
  print(type(a))
  a = int(a)
  print(type(a))

  b = "12.3"
  print(type(b))
  b = float(b)
  print(type(b))
  b = int(b)
  print(type(b))

  # 문자연결 연산자 +
  s1 = "안녕"
  s2 = "하세요"
  print(s1 + s2)
  # 문자열 반복 연산자
  print("-.-" * 20)

  # 문자열 슬라이싱
  str1 = "안녕하세요. 반갑습니다."
  print(str1[0])
  print(str1[6])
  print(str1[2:5]) # [위치 : 위치한칸뒤]
  print(str1[2:5:2]) # [위치 : 위치한칸뒤 : step]
  print(str1[::-1]) # 역순
  
  # input_str = input('글자를 입력하세요.')

  # if input_str == "":
  #   print('글자를 입력하세요')
  # else:
  #   print("입력문자 : ", input_str)
  # print("프로그램이 종료됩니다.")