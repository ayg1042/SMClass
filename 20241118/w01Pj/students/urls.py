from django.urls import path, include
from . import views

# name:url 시 사용
app_name = 'students'

urlpatterns = [
    # 학생 정보 입력
    path('write/', views.write, name='write1'),
    # 학생 리스트
    path('list/', views.list, name='list'),
    # 학생 상세페이지
    # <int:no> 정수일 경우
    path('<str:name>/view/', views.view, name='view'),
    # 학생 정보 수정 1
    path('<str:name>/modify/', views.modify, name='modify'),
    # 학생 정보 수정 2
    path('modify2/', views.modify2, name='modify2'),
    # 학생 정보 수정 3
    path('<str:name>/modify3/', views.modify3, name='modify3'),
    # path('/update', views.update, name='update'),
    # 학생 삭제
    path('<str:name>/delete/', views.delete, name='delete'),
    
    # path('doWrite/', views.doWrite, name='doWrite1'),
]
