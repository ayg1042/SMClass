from django.urls import path, include
from . import views

app_name = 'students'

urlpatterns = [
    path('write/', views.write, name='write'),
    path('list/', views.slist, name='slist'),
    path('<str:name>/view/', views.view, name='view'),
    path('<str:name>/update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
]
