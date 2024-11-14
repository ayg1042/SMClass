from django.urls import path, include
from . import views

urlpatterns = [
    path('event_view/', views.event_view, name='evente_view'),
]
