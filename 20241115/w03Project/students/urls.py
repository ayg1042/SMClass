from django.urls import path, include
from . import views

app_name = 'students'

urlpatterns = [
    path('write/', views.write, name='stu_write'),
    path('stu_save/' ,views.stu_save, name='stu_save'),
    path('list/' ,views.stu_list, name='stu_list'),
]
