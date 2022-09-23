from django.shortcuts import render, redirect
from .forms import NameForm, MusicianForm


# Create your views here.
def index(request):
    return render(request, 'index.html')

def custom_form(request):
    if request.method=='POST':
        name = request.POST['name']
        if name != "홍길동":
           return redirect("custom_form") 
        else:
           return redirect("index")
    # else:
    #     return redirect('index')
    
    return render(request, 'custom_form.html')

def django_form(request):
    if request.method=='POST':
        form = NameForm(request.POST)
        if form.is_valid():         #폼에 정의해둔 제한 조건이 성사되나 판별
                                    #is_valid() 통과 시 cleaned_data 딕셔너리에 값을 담아 줌
            return redirect("index")
        
    else:
        form = NameForm()
    return render(request, "django_form.html",{"form":form})

def musician_create(request):
    if request.method == "POST":
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()     #모델폼을 상속받은 상태이기 떄문에 가능
            return redirect("index")
    else:
        form = MusicianForm()
    return render(request, "musician_register.html", {"form":form})


