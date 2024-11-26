from django.shortcuts import render
from member.models import Member

# Create your views here.
def login(request):
  if request.method == 'GET':
    return render(request, 'login.html')
  else:
    id = request.POST.get('id')
    print(id)
    pw = request.POST.get('pw')
    qs = Member.objects.filter(id=id, pw=pw)
    if qs:
      request.session['session_id'] = qs[0].id
      request.session['session_nicname'] = qs[0].nicname
      return render(request, 'login.html', {'lmsg': '1'})
    else:
      return render(request, 'login.html', {'lmsg': '0'})
    
def logout(request):
  # request.session.delete()
  request.session.clear()
  return render(request, 'index.html', {'omsg': '1'})