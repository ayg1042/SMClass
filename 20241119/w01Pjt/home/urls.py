from django.urls import path
from . import views

# app_name 설정
app_name = ''

urlpatterns = [
    # url 링크, views 함수 호출, name 링크
    path('', views.index, name='index'),
]
