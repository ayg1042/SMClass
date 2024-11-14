from django.urls import path, include
from . import views

app_name = 'students'

urlpatterns = [
    # url 주소, views 함수명
    # localhost/students/reg/
    # students : reg
    path('reg/', views.regStudent, name='reg'),
]
