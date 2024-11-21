from django.shortcuts import render, redirect
from member.models import Member

# Create your views here.
def login(request):
  if request.method == 'GET':
    return render(request, 'login.html')
  else:
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    sq = Member.objects.filter(id = id, pw = pw)
    if sq:
      request.session['session_id'] = sq[0].id
      request.session['session_name'] = sq[0].name
    else:
      data = {'emsg' : '아이디 또는 패스워드가 일치하지 않습니다.'}
      return render(request, 'login.html', data)
    return redirect('/')
  
def logout(request):
  request.session.delete()
  return redirect('/')

def join01(request):
  return render(request, 'join01_terms.html')

def join02(request):
  return render(request, 'join02_info_input.html')

def join03(request):
  return render(request, 'join03_success.html')


