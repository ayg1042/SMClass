from django.contrib import admin
from students.models import Student

# 관리자 페이지에서 컬럼부분 출력
class StudentAdmin(admin.ModelAdmin):
  list_display = ['s_name', 's_major', 's_age']

# Register your models here.
admin.site.register(Student, StudentAdmin)