from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import NameForm, MusicianForm
from .models import Musician
from django.urls import reverse_lazy

# 즉, 내 애플리케이션을 동작하게 하기 위해 CRUD(Create/Read/Update/Delete) 등 함수를 구현하는 곳
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

def musician_list(request):
    """
    musician 전체 리스트 보기 - get 방식
    """
    musician_list = Musician.objects.all()
    
    return render(request, 'musician_list.html',{"musician_list":musician_list})

def musician_detail(request, pk):
    """
    pk에 대항하는 musician 정보 추출
    """
    musician = get_object_or_404(Musician, pk=pk)
    return render(request, 'musician_detail.html', {"musician":musician})

def musician_edit(request, pk):
    
    musician = get_object_or_404(Musician, pk=pk)
    if request.method=="POST":
        pass
    else:
        form = MusicianForm(instance=musician)
    return render(request, "musician_edit.html", {"form":form})

def musician_remove(request,pk):
    musician = get_object_or_404(Musician, pk=pk)
    musician.delete()
    
    return redirect('musician_list')


# 클래스 기반의 뷰
# 1. 제너릭 display view(DetailView, ListView)
class MusicianListView(ListView):
    model = Musician
    template_name = "musician_list.html" # 생략가능 - > 템플릿 밑 폴더 > html 생성해놨을시

class MusicianDetailView(DetailView):  # 함수형 디테일 detail
    model = Musician
    template_name = "musician_detail.html" # 생략가능 - > 템플릿 밑 폴더 > html 생성해놨을시
    
# 클래스 기반의 뷰
# 2. 제너릭 Edit view(CreateView, UpdateView, DeleteView)

class MusicianCreateView(CreateView):   # 함수형 뷰 create()
    
    form_class = MusicianForm
    template_name = 'musician_register.html'
    success_url = reverse_lazy("musician_list_cls")
    
class MusicianUpdateView(UpdateView):
    
    model = Musician
    fields = "__all__"
    template_name = "musician_edit.html"
    success_url = reverse_lazy("musician_list_cls")
    
class MusicianDeleteView(DeleteView):
    model = Musician
    #template_name = "musician_remove.html"
    success_url = reverse_lazy("musician_list_cls")

    #post로 들어왔을 때만 삭제로 정의 되어있기 때문에 get을 다시 정의
    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)