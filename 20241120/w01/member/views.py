from django.shortcuts import render
from member.models import Member

# Create your views here.

# 회원 전체리스트
def mlist(request):
  qs = Member.objects.all()
  data = {'mlist':qs}
  return render(request, 'list.html', data)

# 로그인
## 쿠키정보 검색  : request.COOKIES.get('쿠키 이름')
## 쿠키저장       : response.set_cookie('key', 'value')
## 쿠키삭제       : response.delete_coolie('key')
def login(request):
  if request.method == 'GET':
  # 쿠키 정보
    print('쿠키 정보 : ',request.COOKIES)
    # 쿠키 읽기
    print('cookinifo 정보 : ',request.COOKIES.get('cookinfo'))
    saveId = request.COOKIES.get('saveId', '')
    print('saveId : ', saveId)
    context = {'saveId': saveId}

    response = render(request, 'login.html', context)
    # max_age = 60초 * 60분 1시간
    # 1달 = 60초*60분*24시*30일
    # max_age가 없으면 브라우저 종료시 삭제
    ## 쿠기정보 검색
    if not request.COOKIES.get('cookinfo'):
      # 쿠키 설정(저장)
      response.set_cookie('cookinfo','1111', max_age=60*60)
    return response
  else:
    print('쿠키 정보 : ', request.COOKIES)
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    saveId = request.POST.get('saveId')
    print(f'전달받은 정보 : {id}, {pw}, {saveId}')
    response = render(request, 'login.html')
    # 아이디 기억하기 정보가 있으면
    if saveId is not None:
      response.set_cookie('saveId', id, max_age=60*60) # 아이디기억하기 체크가 있으면 쿠키저장
    else:
      response.delete_cookie('saveId') # 아이디기억하기 체크가 없으면 쿠키삭제
    return response

def login2(request):
  if request.method == 'GET':
    cookeId = request.COOKIES.get('cookeId')
    data = {'cookeId':cookeId}
    return render(request, 'login2.html', data)
  else:
    response = render(request, 'index.html')
    # 3개의 정보
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    saveId = request.POST.get('saveId')
    if saveId is not None:
      response.set_cookie('cookeId', id, max_age=60*60)
    else:
      response.delete_cookie('cookeId')
    print(id, pw, saveId)
    return response

def product(request):
  if request.method == 'GET':
    # 쿠키 읽어오기
    c_pId = request.COOKIES.get('c_pId', '')
    c_pName = request.COOKIES.get('c_pName', '')
    print('데이터 : ', c_pId, c_pName)
    context = {'c_pId':c_pId, 'c_pName':c_pName}
    return render(request, 'product.html', context)
  else:
    # 쿠키저장
    pId = request.POST.get('pId')
    pName = request.POST.get('pName')
    pOption = request.POST.get('pOption')
    saveProduct = request.POST.get('saveProduct')
    response = render(request, 'index.html')
    print(pId, pName, pOption, saveProduct)
    if saveProduct is not None: # 체크가 되어있으면
      # 쿠키설정
      response.set_cookie('c_pId', pId)
      response.set_cookie('c_pName', pName)
    else:
      response.delete_cookie('c_pId')
      response.delete_cookie('c_pName')
    return response

def product2(request):
  cooke_data = request.COOKIES.get('saveCoPro')
  print('데이터 확인 : ',cooke_data)
  data = {'cooke_data': cooke_data}
  if request.method == 'GET':
    return render(request, 'product.html', data)
  else:
    response = render(request, 'product.html', data)
    pId = request.POST.get('pId')
    pName = request.POST.get('pName')
    pOption = request.POST.get('pOption')
    saveProduct = request.POST.get('saveProduct')
    if saveProduct:
      response.set_cookie('saveCoPro', pId, max_age=60*60)
    else:
      response.delete_cookie('saveCoPro')
    print(pId, pName, pOption)
    return response

def m2(request):
  c_memberId = request.COOKIES.get('c_memberId', '')
  c_money = request.COOKIES.get('c_money', '')
  if c_memberId:
    print('데이터 확인 : ',c_memberId)
    data = {'c_memberId': c_memberId, 'c_money': c_money}
  else:
    data = {}

  if request.method == 'GET':
    return render(request, 'm2.html', data)
  else:
    response = render(request, 'm2.html', data)
    memberId = request.POST.get('memberId')
    money = request.POST.get('money')
    option = request.POST.get('option')
    saveMember = request.POST.get('saveMember')
    if saveMember:
      response.set_cookie('c_memberId', memberId, max_age=60*60)
      response.set_cookie('c_money', money, max_age=60*60)
    else:
      response.delete_cookie('c_memberId')
      response.delete_cookie('c_money')
    print(memberId, money, option)
    return response
