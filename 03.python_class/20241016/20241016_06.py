import os

if not os.path.exists('c:/bbb'):
  os.makedirs('c:/bbb')
  print('폴더가 없습니다.')
else:
  print('폴더가 있습니다.')

f = open('c:/bbb/c.txt', 'w', encoding='utf-8')
f.write('안녕하세요.')