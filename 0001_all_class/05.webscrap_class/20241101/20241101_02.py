import datetime

print(datetime.datetime.now().year)
now_year = datetime.datetime.now().year

# in_year = input('생일입력 : 20020312 ')
in_year = '19960312'
print(in_year)
print()

print(f'현재 나이 : {now_year - int(in_year[:4])}')