from django.shortcuts import render, redirect
from students.models import Student

# Create your views here.
# 학생 추가
def write(request):
  if request.method == 'GET':
    return render(request, 'write.html')
  else:
    name = request.POST['name']
    major = request.POST['major']
    grade = request.POST['grade']
    age = request.POST['age']
    gender = request.POST['gender']
    hobby = request.POST.getlist('hobby')
    Student.objects.create(name=name, major=major, grade=grade, age=age, gender=gender, hobby=hobby)
    return redirect('/students/list')

# 학생출력
def slist(request):
  qs = Student.objects.all()
  data = {'slist': qs}
  return render(request, 'list.html', data)

# 상세정보
def view(request, name):
  qs = Student.objects.get(name=name)
  data = {'stu':qs}
  return render(request, 'view.html', data)

# 정보수정
def update(request, name):
  if request.method == 'GET':
    qs = Student.objects.get(name=name)
    data = {'stu':qs}
    return render(request, 'update.html', data)
  else:
    print(name)
    qs = Student.objects.get(name=name)
    qs.name = request.POST['name']
    qs.major = request.POST['major']
    qs.grade = request.POST['grade']
    qs.age = request.POST['age']
    qs.gender = request.POST['gender']
    qs.hobby = request.POST.getlist('hobby')
    qs.save()
    return redirect('/students/list')

# 정보 삭제
def delete(request):
  id = request.GET['id']
  qs = Student.objects.get(id=id).delete()
  return redirect('/students/list')




