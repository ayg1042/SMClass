from django.contrib import admin
from students.models import Student
# Register your models here.

# admin창에서 출력되는 데이터 리스트
class StudentAdmin(admin.ModelAdmin):
  list_display = ['name', 'major', 'grade', 'age', 'gender']

# admin에 등록
admin.site.register(Student, StudentAdmin)