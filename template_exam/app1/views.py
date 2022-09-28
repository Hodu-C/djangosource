from django.shortcuts import render

# Create your views here.
def list(request):
    return render(request, 'app1/list.html')
def detail(request):
    return render(request, 'app1/detail.html')

