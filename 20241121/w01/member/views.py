from django.shortcuts import render,redirect
from member.models import Member

# Create your views here.
# 1. 로그인 페이지
# 2. 로그인 버튼
def login(request):
  if request.method == 'GET':
    return render(request, 'login.html')
  else:
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    qs = Member.objects.filter(id=id, pw=pw)
    if qs:
      msg = '로그인이 되었습니다.'
      print(msg)
      # 세션연결
      request.session['session_id'] = id
      request.session['session_nicname'] = qs[0].nicname
      return redirect('/')
    else:
      msg = '아이디 또는 패스워드가 일치하지 않습니다.'
      print(msg)
      return render(request, 'login.html', {'login_msg': msg})
    
def logout(request):
  request.session.clear() # 전체세션 삭제
  # del request.session.['session_id'] # 해당 세션 삭제
  return redirect('/')

# 회원 리스트
def mlist(request):
  id = request.session['session_id']
  if id == 'admin':
    qs = Member.objects.all()
    data = {'members':qs}
  else:
    qs = Member.objects.filter(id = id)
    print(qs[0].id)
    data = {'members':qs}
  return render(request, 'mlist.html', data)

def mview(request, id):
  print('아이디 : ', id)
  qs = Member.objects.filter(id=id)
  context = {'mem':qs[0]}
  return render(request, 'mview.html', context)

def mupdate(request, id):
  if request.method == 'GET':
    print('수정 아이디 : ', id)
    qs = Member.objects.get(id = id)
    data = {'mem':qs}
    return render(request, 'mupdate.html', data)
  else:
    print('id = ',id)
    id = request.session['session_id']
    if id == 'admin':
      id = request.POST.get('id')
    pw = request.POST.get('pw')
    name = request.POST.get('name')
    nicname = request.POST.get('nicname')
    tel = request.POST.get('tel')
    gender = request.POST.get('gender')
    hobbys = request.POST.getlist('hobby')
    hobby = ','.join(hobbys)
    # print(id, pw, name, nicname, tel, gender, hobby)
    qs = Member.objects.get(id=id)
    qs.id = id
    qs.pw = pw
    qs.name = name
    qs.nicname = nicname
    qs.tel = tel
    qs.gender = gender
    qs.hobby = hobby
    qs.save()
    return redirect('member:mlist')

def mwrite(request):
  if request.method == 'GET':
    return render(request, 'mwrite.html')
  else:
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    name = request.POST.get('name')
    nicname = request.POST.get('nicname')
    tel = request.POST.get('tel')
    gender = request.POST.get('gender')
    hobbys = request.POST.getlist('hobby')
    hobby = ','.join(hobbys)
    # qs = Member(id=id, pw=pw, name=name, nicname=nicname, tel=tel, gender=gender, hobby=hobby)
    # qs.save()
    qs = Member.objects.create(id=id, pw=pw, name=name, nicname=nicname, tel=tel, gender=gender, hobby=hobby)
    return redirect('/member/mlist')
    # return redirect('member:mlist')

def mdelete(request, id):
  Member.objects.get(id=id).delete()
  return redirect('member:mlist')






