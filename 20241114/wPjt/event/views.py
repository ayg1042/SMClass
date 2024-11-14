from django.shortcuts import render
from . import views

# Create your views here.
def event_view(request):
  return render(request, 'event_view.html')