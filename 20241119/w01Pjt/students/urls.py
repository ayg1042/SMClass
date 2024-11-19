from django.urls import path
from . import views

# app_name 설정
app_name = 'students'

urlpatterns = [
    # url 링크, views 함수 호출, name 링크
    path('write/', views.write, name='write'),
    path('search/', views.search, name='search'),
    path('list/', views.Slist, name='list'),
    path('<str:name>/view/', views.view, name='view'),
    # path('<str:name>/delete/', views.delete, name='delete'),
    path('delete/<str:name>/', views.delete, name='delete'),
    path('update/', views.update, name='update'), # 파라미터
    path('<str:name>/update/', views.update2, name='update2'),
]
