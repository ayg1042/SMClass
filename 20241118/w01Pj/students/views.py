from django.shortcuts import render, redirect
from students.models import Student

# Create your views here.

# 학생입력 페이지 호출
def write(request):
  if request.method == 'GET':
    print("GET방식으로 들어옴")
    return render(request, 'write.html')
  else:
    print("POST방식으로 들어옴")
    name = request.POST['name']
    major = request.POST['major']
    grade = request.POST['grade']
    age = request.POST['age']
    gender = request.POST['gender']
    print('입력데이터 : ', name, major, grade, age, gender)
    Student.objects.create(name=name, major=major, grade=grade, age=age, gender=gender)
    return redirect('students:list')

def list(request):
  qs = Student.objects.all()
  context = {'slist':qs}
  return render(request, 'list.html', context)

def view(request, name):
  print('이름 정보', name)
  # 해당 방법은 없는 경우 에러가 나온다.
  # qs = Student.objects.get(name = name)
  # 위와 같은 결과가 나온다. 해당 방법은 빈칸이 넘어온다.
  qs = Student.objects.filter(name = name) # 1개 데이터 list타입, 없는 데이터{}
  # qs = Student.object_or_404(Student, name = name) # 없을경우 구문리턴
  context = {'stu': qs[0]}
  return render(request, 'view.html', context)

# 학생수정 페이지 1 - url 매개변수로 데이터값을 전달받음
def modify(request, name):
  if request.method == 'GET':
    print('modify1의 이름 정보 :', name)
    # 1개 데이터 가져오기
    sq = Student.objects.filter(name=name)
    context = {'stu':sq[0]}
    return render(request, 'update.html', context)
  else:
    print('POST 호출입니다.')
    sq = Student.objects.get(name=name)
    name = request.POST['name']
    major = request.POST['major']
    grade = request.POST['grade']
    age = request.POST['age']
    gender = request.POST['gender']
    print('수정될 데이터 : ',name, major, grade, age, gender)
    print('기존 데이터 : ', sq.name, sq.major, sq.grade, sq.age)
    # db저장
    sq.major = major
    sq.grade = grade
    sq.age = age
    sq.gender = gender
    sq.save()
    return redirect('students:list')

def delete(request, name):
  print('삭제정보 : ', name)
  qs = Student.objects.get(name = name)
  return redirect('students:list')


def update(request):
  return render(request, 'index.html')


# 학생수정 페이지 2 - 파라미터
def modify2(request):
  name = request.GET.get('name')
  print('modify2의 이름 정보 :', name)
  sq = Student.objects.filter(name=name)
  context = {'stu':sq[0]}
  return render(request, 'update.html', context)

# 학생수정 페이지 3 - AppName 매개변수로 데이터값을 전달받음
def modify3(request, name):
  print('modify3의 이름 정보 :', name)
  sq = Student.objects.filter(name=name)
  context = {'stu':sq[0]}
  return render(request, 'update.html', context)



# 학생 입력 저장
# def doWrite(request):
#   if request.method == 'POST':
#     name = request.POST['name']
#     major = request.POST['major']
#     grade = request.POST['grade']
#     age = request.POST['age']
#     gender = request.POST['gender']
#     print('입력데이터 : ', name, major, grade, age, gender)
#   else:
#     print('해당되는 데이터가 없습니다.')
#   return redirect('/')