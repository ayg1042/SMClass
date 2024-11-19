from django.urls import path, include
from . import views

# name:url 시 사용
app_name = ''

urlpatterns = [
    path('', views.index, name='index'),
]
