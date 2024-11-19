from django.db import models

# Create your models here.
class Student(models.Model):
  # 따로 지정해주지 않으면 자동으로 생성됨 => id
  name = models.CharField(max_length=100)
  major = models.CharField(max_length=100)
  grade = models.IntegerField(default=1)
  age = models.IntegerField(default=1)
  gender = models.CharField(max_length=10)
  hobby = models.CharField(max_length=50)

  def __str__(self):
    return f'{self.name}, {self.major}, {self.grade}'