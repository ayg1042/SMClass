from django.shortcuts import render, redirect
from board.models import Board
from django.db.models import Max
from django.contrib import messages
from django.db.models import F

# Create your views here.
# 게시판 글 쓰기
def bwrite(request):
  if request.method == 'GET':
    return render(request, 'bwrite.html')
  else:
    id = request.POST.get('id')
    btitle = request.POST.get('btitle')
    bcontent = request.POST.get('bcontent')

    qs = Board.objects.create(id=id, btitle=btitle, bcontent=bcontent)
    qs.bgroup = qs.bno
    qs.save()
    # 1회 노출된다
    messages.success(request, message='게시글이 저장되었습니다.')
    # return redirect('board:blist')
    return render(request, 'bwrite.html', {'w_msg':'1'})

# 게시판 리스트
def blist(request):
  qs = Board.objects.all().order_by('-bgroup', 'bstep')
  context = {'blist':qs}
  return render(request, 'blist.html', context)

# 글상세보기
def bview(request, bno):
  print('게시글 번호 : ', bno)
  # 조회수 증가 filter 방식 update()
  # 여러개가 검색되면 한번에 불러와서 업데이트 가능하다.
  qs = Board.objects.filter(bno = bno)
  # F함수, 검색된 값을 가져오기
  if len(qs) < 1:
    return render(request, 'bview.html')
  qs.update(bhit=F('bhit') + 1)
  context = {'board':qs[0]}
  
  # 조회수 증가 get 방식 save 해야함
  # qs = Board.objects.get(bno = bno)
  # qs.bhit = qs.bhit + 1
  # qs.save()
  # context = {'board':qs}
  return render(request, 'bview.html', context)

# 글 수정 페이지, 글 수정 저장
def bmodify(request, bno):
  if request.method == 'GET':
    qs = Board.objects.filter(bno=bno)
    context = {'board': qs[0]}
    return render(request, 'bmodify.html', context)
  else:
    id = request.POST.get('bname')
    btitle = request.POST.get('btitle')
    bcontent = request.POST.get('bcontent')
    qs = Board.objects.get(bno = bno)
    qs.btitle = btitle
    qs.bcontent = bcontent
    qs.save()
    # return redirect('board:blist')
    return render(request, 'bmodify.html', {'u_msg':bno})

# 글 삭제
def bdelete(request, bno):
  print('게시글 번호 : ', bno)
  Board.objects.get(bno=bno).delete()
  # return redirect('board:blist')
  return render(request, 'blist.html', {'d_msg': bno})

# 답변달기
def breply(request, bno):
  if request.method == 'GET':
    print('게시글 번호 : ', bno)
    qs = Board.objects.get(bno = bno)
    return render(request, 'breply.html', {'board': qs})
  else:
    bgroup = int(request.POST.get('bgroup'))
    bstep = int(request.POST.get('bstep'))
    bindent = int(request.POST.get('bindent'))
    id = request.POST.get('id')
    btitle = request.POST.get('btitle')
    bcontent = request.POST.get('bcontent')
    # 다른 답변달기에 bstep에 1증가
    qs = Board.objects.filter(bgroup=bgroup, bstep__gt=bstep)
    qs.update(bstep = F('bstep') + 1)

    # bgroup은 부모의 bgroup을 입력
    Board.objects.create(id=id, btitle=btitle, bcontent=bcontent, bgroup=bgroup, bstep=bstep+1, bindent=bindent+1)

    print('그룹 번호 :', bgroup)
    # return redirect('board:blist')
    return render(request, 'blist.html', {'r_msg':'1'})


