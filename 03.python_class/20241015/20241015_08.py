from SS import *
from math import *
from urllib import request

target = request.urlopen("http://google.com")
output = target.read()

print(output)

# stu_output()
# print(s_title)

# print(floor(1.23)) # 버림
# print(ceil(1.23)) # 올림
# print(round(1.23)) # 반올림