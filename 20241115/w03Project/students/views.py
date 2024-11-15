from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from students.models import Student

# Create your views here.
# 학생 정보 입력
def write(request):
  return render(request, 'stu_write.html')

# 학생 정보 출력
def stu_list(request):
  qs = Student.objects.all()
  context = {'list': qs}
  return render(request, 'stu_list.html', context)

# 학생 정보 저장
def stu_save(request):
  print('전송 데이터 확인')
  print(request.POST)
  print(request.GET)
  if request.POST:
    name = request.POST['name']
    major = request.POST['major']
    grade = request.POST['grade']
    age = request.POST['age']
    gender = request.POST['gender']
    qs = Student(s_name=name, s_major=major, s_grade=grade, s_age=age, s_gender=gender)
    qs.save()
    print('데이터 저장이 되었습니다.')
  return HttpResponseRedirect(reverse('index'))