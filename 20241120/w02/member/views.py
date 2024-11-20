from django.shortcuts import render, redirect
from member.models import Member

# Create your views here.
def mlist(request):
  return render(request, 'mlist.html')

def cookWrite(request):
  response = render(request, 'cookWrite.html')
  if request.method == 'GET':    
    print('GET 방식으로 들어옴')
    return response
  else:
    response = render(request, 'index.html')
    print('POST 방식으로 들어옴')
    ckey = request.POST.get('ckey')
    cvalue = request.POST.get('cvalue')
    response.set_cookie(ckey, cvalue)
    return response
  
def cookDelete(request):
  if request.method == 'GET':
    response = render(request, 'cookDelete.html')
  else:
    response = render(request, 'index.html')
    ckey = request.POST.get('ckey')
    response.delete_cookie(ckey)
    print(ckey, '쿠키가 삭제되었습니다.')
  return response

def login(request):
  if request.method == 'GET':
    response = render(request, 'login.html')
  else:
    emsg = ''
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    qs = Member.objects.filter(id=id, pw=pw)
    if qs:
      context = {'emsg':emsg, 'member':qs[0]}
      request.session['session_id'] = id
      request.session['session_nicname'] = qs[0].nicname
      response = render(request, 'index.html', context)
    else:
      emsg = '아이디 또는 패스워드가 일치하지 않습니다.'
      context = {'emsg':emsg, 'member': ''}
      response = render(request, 'login.html', context)
  return response

def logout(request):
  request.session.clear() # 섹션 모두 삭제
  # del request.session['session_id'] # 해상 섹션만 삭제
  return redirect('/')

