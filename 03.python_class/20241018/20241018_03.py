class car:
  # color = ''
  # speed = 0

  def __init__(self):
    self.color = '흰색'
    self.tire = 4
    self.speed = 0
    self.gear = 'auto'
  

  def upSpeed(self, value):
    if value > 0: self.speed += value
    else: print('값을 잘못 넣었습니다.')

  def downSpeed(self, value):
    if value < 0: self.speed -= value
    else: print('값을 잘못 넣었습니다.')

class sp_car(car):
  pass
c2 = car()
c2.color = '빨강'
print(c2.color)
c2.upSpeed(-10)