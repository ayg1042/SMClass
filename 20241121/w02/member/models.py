from django.db import models

# Create your models here.
class Member(models.Model):
  id = models.CharField(max_length=20, primary_key=True)
  pw = models.CharField(max_length=100)
  name = models.CharField(max_length=50)

  def __str__(self):
    return f'{self.id}, {self.pw}, {self.name}'