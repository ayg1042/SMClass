from django.db import models

# Create your models here.
class Student(models.Model):
  s_name = models.CharField(max_length=200)
  s_major = models.CharField(max_length=200)
  s_age = models.IntegerField(default=0)
  s_grade = models.IntegerField(default=0)
  s_gender = models.CharField(max_length=2)

  def __str__(self):
    return self.s_name