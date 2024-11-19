from django.shortcuts import render, redirect
from students.models import Student
from django.urls import reverse
# Create your views here.

# 학생입력페이지, 학생저장
def write(request):
  # templates 폴더에서 html파일을 검색한다.
  if request.method == 'POST':
    # name = request.objects.get('name') #이렇게도 받을 수 있음
    # request.objects.get('data') # data가 없을경우 None
    # reqeust.POST['data'] # data가 없을경우 error
    name = request.POST['name']
    major = request.POST['major']
    grade = request.POST['grade']
    age = request.POST['age']
    gender = request.POST['gender']
    # hobby = request.POST['hobby'] # hobby의 경우 방식이 다르다.
    # checkbox 데이터 가져오기~
    hobbys = request.POST.getlist('hobby') # hobby의 경우 방식이 다르다. 여러개 받는법
    # getlist -> type(list)
    # hobby = ','.join(hobbys)
    # hobby_list = hobby.split(',')
    # print(hobby)
    # print(hobbys)
    Student.objects.create(name=name, major=major, grade=grade, age=age, gender=gender, hobby=hobbys)
    return redirect('/students/list/')
  else: # GET일 경우
    return render(request, 'write.html')

# 학생검색
def search(request):
  search = request.GET.get('search')
  print('검색 단어 : ',search)
  # 검색기능
  # qs = Student.objects.filter(name=search)# 정확하게 일치
  qs = Student.objects.filter(name__contains=search) # 하나라도 있다면
  data = {'slist':qs}
  return render(request, 'list.html', data)


def Slist(request):
  # 학생 전체정보 가져오기
  # ps = Student.objects.all()
  # ps = Student.objects.order_by('grade') # 정렬
  ps = Student.objects.order_by('-grade', 'name') # 역순정렬
  data ={'slist':ps}
  return render(request, 'list.html', data)

def view(request, name):
  qs = Student.objects.get(name = name)
  data = {'stu':qs}
  return render(request, 'view.html', data)

# 학생정보 삭제
def delete(request, name):
  print('삭제할 데이터 : ',name)
  # Student.objects.delete(name=name)
  Student.objects.get(name=name).delete()
  return redirect('/students/list')

# 학생수정페이지, 학생수정저장
def update(request):
  if request.method == 'GET':
    name = request.GET['name']
    print('?= 방식 GET ',name)
    qs = Student.objects.get(name=name)
    data = {'stu':qs}
    return render(request,'update.html', data)
  else:
    name = request.POST['name']
    major = request.POST['major']
    grade = request.POST['grade']
    age = request.POST['age']
    gender = request.POST['gender']
    hobby = request.POST.getlist('hobby')
    qs = Student.objects.get(name = name)
    qs.major = major
    qs.grade = grade
    qs.age = age
    qs.gender = gender
    qs.hobby = hobby
    qs.save()
    print('?= 방식 POST ',name)
    return redirect('students:view', name)
    # return redirect(reverse('students:view', args=(name,)))
    # return redirect(reverse('students:list'))

def update2(request, name):
  if request.method == 'GET':
    print('url 방식 GET ', name)
    qs = Student.objects.get(name=name)
    data = {'stu':qs}
    return render(request,'update.html', data)
  else:
    print('url 방식 POST ', name)
    return redirect(reverse('students:list'))


