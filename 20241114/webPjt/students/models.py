from django.db import models

# Create your models here.
# 오라클에서 table 생성가능, insert, update, select, delete
# 오라클에 접속하지 않고, table 생성 가능
# orm 방식을 사용한다.(Object-Relational Mapping)
# 객체 관계형 매핑

# Student 테이블 생성
class Student(models.Model):
  s_name = models.CharField(max_length=100)
  s_major = models.CharField(max_length=100)
  s_age = models.IntegerField(default=0)
  s_grade = models.IntegerField(default=0)
  s_gender = models.CharField(max_length=30)

  def __str__(self):
    return self.s_name