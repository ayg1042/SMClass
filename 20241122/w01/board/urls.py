from django.urls import path, include
from . import views

app_name = 'board'

urlpatterns = [
    path('bwrite/', views.bwrite, name='bwrite'),
    path('bview/<int:bno>', views.bview, name='bview'),
    path('breply/<int:bno>', views.breply, name='breply'),
    path('bdelete/<int:bno>', views.bdelete, name='bdelete'),
    path('bmodify/<int:bno>', views.bmodify, name='bmodify'),
    path('blist/', views.blist, name='blist'),
]
