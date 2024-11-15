from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from students.models import Student

# Create your views here.

# 학생 데이터 출력
def list(request):
  qs = Student.objects.all()
  # 정보전달 변수생성
  context = {'list':qs}

  return render(request, 'stu_list.html', context)


# 등록 페이지 이동
def write(request):
  print('학생 등록 페이지')
  return render(request, 'stu_write.html')


# 학생 저장
def save(request):
  # home에 있는 index로 이동한다.
  print('학생 정보 저장 호출')
  # if request.POST: # request.POST 데이터가 있는지
  if request.method == 'POST': # POST방식으로 전달이 되었는지.
    print('post2')
    name = request.POST['name']
    major = request.POST['major']
    grade = request.POST['grade']
    age = request.POST['age']
    gender = request.POST['gender']
    # print(name, major, grade, age, gender)
    qs = Student(s_name=name, s_major=major, s_grade=grade, s_age=age, s_gender=gender)
    qs.save()



  # redirect('/')
  # return redirect('index')
  # reverse 를 사용하면 App_name을 사용할 수 있다.
  # return redirect(reverse('index'))
  return HttpResponseRedirect(reverse('index'))