from django.shortcuts import render, get_object_or_404,redirect
from .forms import TodoForm
from .models import Todo

# Create your views here.
def index(request):
    return render(request, "index.html")

def todo_list(request):
    #todos= Todo.objects.all()
    
    todos = Todo.objects.filter(complete=False)
    
    return render(request, "todo_list.html", {"todos":todos})

def todo_detail(request, pk):
    
    todo = get_object_or_404(Todo, pk=pk)
    
    return render(request, "todo_detail.html", {"todo":todo})

def todo_create(request):
    if request.method=="POST":
        form = TodoForm(request.POST)
        if form.is_valid(): #모델 규칙 검증해줌
            todo = form.save()
            return redirect("todo_detail",pk=todo.pk)
    else:
        form = TodoForm()
    return render(request,"todo_register.html",{"form":form})

def todo_edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("todo_list")
    else:
        form = TodoForm(instance=todo)
        
    return render(request, "todo_edit.html", {"form":form})

def todo_done(request, pk):
    
    todo = get_object_or_404(Todo,pk=pk)
    todo.complete = True
    todo.save()
    
    return redirect("todo_list")


def done_list(request):
    dones = Todo.objects.filter(complete=True)
    
    return render(request, "done_list.html", {"dones":dones})