from django.shortcuts import render, redirect
from students.models import Student

# Create your views here.
def write(request):
  if request.method == "GET":
    print('GET')
    return render(request, 'write.html')
  else:
    name = request.POST['name']
    major = request.POST['major']
    grade = request.POST['grade']
    age = request.POST['age']
    gender = request.POST['gender']
    Student.objects.create(name=name, major=major, grade=grade, age=age, gender=gender)
    return redirect('/')

def slist(request):
  qs = Student.objects.all()
  data = {'list':qs}
  return render(request, 'list.html', data)