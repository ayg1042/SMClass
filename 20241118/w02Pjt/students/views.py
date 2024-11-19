from django.shortcuts import render

# Create your views here.
def write(request):
  return render(request, 'write.html')


def list(request):
  return render(request, 'list.html')


def view(request):
  return render(request, 'view.html')