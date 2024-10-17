product = [
  {"pno":1,"pCode":"t001","pName":"삼성TV","price":2000000,"color":"black"},
  {"pno":2,"pCode":"g001","pName":"LG냉장고","price":3000000,"color":"white"},
  {"pno":3,"pCode":"h001","pName":"하만카돈스피커","price":500000,"color":"gray"},
  {"pno":4,"pCode":"w001","pName":"세탁기","price":1000000,"color":"yellow"},
]

def product_save(product):
  f = open('product.txt', 'w', encoding='utf-8')
  for i in product:
    f.write(f'{i['pno']},{i['pCode']},{i['pName']},{i['price']},{i['color']}\n')
  print('product 내용 저장이 완료되었습니다.')
  f.close()

product_save(product)