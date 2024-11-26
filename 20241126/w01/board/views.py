from django.shortcuts import render
from board.models import Board
from member.models import Member
from datetime import datetime
from django.db.models import Q
from django.db.models import F
from django.core.paginator import Paginator

# Create your views here.

def breply(request, bno):
  if request.method == 'GET':
    qs = Board.objects.get(bno = bno)
    return render(request, 'breply.html', {'board': qs})
  else:
    id = request.session.get('session_id')
    member = Member.objects.get(id=id)
    bno = request.POST.get('bno')
    bgroup = int(request.POST.get('bgroup'))
    bstep = int(request.POST.get('bstep'))
    bindent = int(request.POST.get('bindent'))

    qs = Board.objects.filter(bgroup=bgroup, bstep__gt=bstep)
    qs.update(bstep = F('bstep') + 1)

    btitle = request.POST.get('btitle')
    bcontent = request.POST.get('bcontent')
    bfile = request.FILES.get('bfile', '')
    Board.objects.create(member=member, btitle=btitle, bcontent=bcontent, bfile=bfile, bgroup=bgroup, bstep=bstep + 1, bindent=bindent + 1)

    return render(request, 'breply.html', {'rmsg': bno})

def bupdate(request, bno):
  if request.method == 'GET':
    qs = Board.objects.get(bno = bno)
    return render(request, 'bupdate.html', {'board': qs})
  else:
    bno = request.POST.get('bno')
    btitle = request.POST.get('btitle')
    bcontent = request.POST.get('bcontent')
    bfile = request.FILES.get('bfile', '')
    # 게시글 저장
    qs = Board.objects.get(bno=bno)
    qs.btitle = btitle
    qs.bcontent = bcontent
    if bfile != '':
      qs.bfile = bfile
    qs.save()
    return render(request, 'bupdate.html', {'umsg': bno})


def bdelete(reqeust, bno):
  qs = Board.objects.get(bno=bno)
  qs.delete()
  return render(reqeust, 'blist.html', {'dmsg': bno})

def bview(request, bno):
  npage = request.GET.get('npage', 1)
  qs = Board.objects.get(bno = bno)

  # 이전글, 다음글
  prev_qs = Board.objects.filter(Q(bgroup__lt = qs.bgroup, bstep__lte=qs.bstep) | Q(bgroup=qs.bgroup, bstep__gt=qs.bstep)).order_by('-bgroup', 'bstep').first()
  next_qs = Board.objects.filter(Q(bgroup__gt = qs.bgroup, bstep__gte=qs.bstep) | Q(bgroup=qs.bgroup, bstep__lt=qs.bstep)).order_by('bgroup', '-bstep').first()

  # 날짜 설정 - 쿠키 시간 사용
  day1 = datetime.replace(datetime.now(), hour=23, minute=59, second=59)
  expires = datetime.strftime(day1, '%a, %d-%b-%Y %H:%M:S GMT')
  print('날짜 : ', expires)

  response = render(request, 'bview.html', {'board':qs, 'prev_board':prev_qs, 'next_board':next_qs, 'npage':npage})
  # 쿠키 확인
  if request.COOKIES.get('cookie_boardNo') is not None:
    cookies = request.COOKIES.get('cookie_boardNo')
    cookies_list = cookies.split('|')
    if str(bno) not in cookies_list:
      response.set_cookie('cookie_boardNo', cookies + f'|{bno}', expires=expires)
      qs.bhit += 1
      qs.save()
  else:
    # 쿠키 저장
    response.set_cookie('cookie_boardNo', bno, expires=expires)
    qs.bhit += 1
    qs.save()
  return response

def blist(request):
  npage = int(request.GET.get('npage', 1))# 넘어온 현재페이지
  qs = Board.objects.all().order_by('-bgroup', 'bstep')
  # 하단 페이지 처리(넘버링)
  paginator = Paginator(qs, 10)
  blist = paginator.get_page(npage)
  return render(request, 'blist.html', {'blist': blist, 'npage':npage})

def bwrite(request):
  if request.method == 'GET':
    return render(request, 'bwrite.html')
  else:
    id = request.session['session_id']
    # id = request.session.get('session_id')
    btitle = request.POST.get('btitle')
    bcontent = request.POST.get('bcontent')
    bfile = request.FILES.get('bfile', '')
    print('파일정보 : ', bfile)
    member = Member.objects.get(id=id)
    # 게시글 저장
    qs = Board.objects.create(member=member, btitle=btitle, bcontent=bcontent, bfile=bfile)
    qs.bgroup = qs.bno
    qs.save()

    return render(request, 'bwrite.html', {'wmsg': '1'})